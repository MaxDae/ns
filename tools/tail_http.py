from datetime import datetime
from optparse import OptionParser
import os
import re
import sys
import time
import urllib3
import urlparse

"""
This script acts like Unix "tail -f", but can watch files over HTTP.
It supports simple HTTP authentication. A known issue is that it will sometimes
display a duplicate character at the start of a line e.g. "200" will become
"2200".
"""

LOG_USERNAME = ""
LOG_PASSWORD = ""

DEFAULT_LOG_INCLUDE_PATTERNS = ""

FILE_URL_PATTERN = "<a href=\"(.+?)\"><tt>.+?\..+?</tt></a>"

SERVER_MAPPINGS = {
    "beta": "",
    "beta2": "",
    "stagingsvr1": "",
    "testserver": "",
    "df1": "",
    "df2": "",
    "df3": "",
    "df4": "",
    "df5": "",
}

def extract_log_urls(html, fileURLPattern, includePatterns=None):
    allFilenames = re.findall(fileURLPattern, html, re.MULTILINE)

    # Filtering
    if includePatterns:
        splitIncludePatterns = [pat.strip() for pat in includePatterns.split(",")]
        selectedFilenames = []
        for filename in allFilenames:
            if any(pat in filename for pat in splitIncludePatterns):
                selectedFilenames.append(filename)
    else:
        selectedFilenames = allFilenames
    return selectedFilenames

def get_log_filenames(serverURL, username, password, includePatterns=None):
    reqHeaders = urllib3.make_headers(basic_auth=username+":"+password)
    logIndexURL = urlparse.urljoin(serverURL, "/logs")
    connPool = urllib3.connection_from_url(logIndexURL)
    getResp = connPool.urlopen(method="GET",
                                url=logIndexURL,
                                headers=reqHeaders)
    logIndexHTML = getResp.data
    logRelativeURLs = extract_log_urls(logIndexHTML,
                                        FILE_URL_PATTERN,
                                        includePatterns)
    urls = [urlparse.urljoin(serverURL, logFileURL)
                for logFileURL in logRelativeURLs]
    return urls

class LogFileTailer(object):
    def __init__(self, url, username, password, outputDir=None):
        self.url = url
        self.lastLength = None
        self.lastETag = None
        self.reqHeaders = urllib3.make_headers(basic_auth=username+":"+password,
                                                    keep_alive=True)
        self.connPool = urllib3.connection_from_url(self.url)
        # File output
        if outputDir:
            if not os.path.exists(outputDir):
                raise OSError, "directory can't be accessed: %s" % outputDir
            # If the seenChanges flag is false the file will be overwritten
            # if it exists. If it's true the file will be appended to.
            self.seenChanges = False
            logFilename = os.path.basename(url)
            serverName = urlparse.urlparse(url).netloc
            self.outputFilePath = os.path.join(outputDir, serverName + "_" + logFilename)
            print "Writing output to %s" % self.outputFilePath
        else:
            self.outputFilePath = None

    def __get_length_and_etag(self):
        try:
            resp = self.connPool.urlopen(method="HEAD",
                                        url=self.url,
                                        headers=self.reqHeaders)
        except urllib3.connectionpool.MaxRetryError:
            print "Connection failed at %s" % datetime.now().strftime("%Y-%m-%d %I:%M %p")
            raise
        headers = resp.headers
        try:
            length = int(headers["content-length"])
            ETag = headers["etag"]
        except KeyError:
            print "Headers: %s" % headers
            print "Header not found at %s" % datetime.now().strftime("%Y-%m-%d %I:%M %p")
            raise
        return length, ETag

    def store_initial_length_and_etag(self):
        self.lastLength, self.lastETag = self.__get_length_and_etag()
        lastLengthMB = round(float(self.lastLength) / 1024 / 1024, 2)
        print "  Initial length for %s: %s (%s MB)" % (self.url, self.lastLength, lastLengthMB)

    def check_for_changes(self):
        length, ETag = self.__get_length_and_etag()
        if length > self.lastLength and ETag != self.lastETag:
            return (length, ETag)
        elif length == self.lastLength and ETag == self.lastETag:
            return (None, None)
        else:
            raise ValueError, "Unhandled case. Debug info: lastLength=%s, length=%s, lastETag=%s, ETag=%s" % \
            (self.lastLength, length, ETag, self.lastETag)

    def download_and_output_new_data(self, length, ETag):
        """
        Does 3 things: gets new data, prints/writes new data,
        and re-sets the lastLength and lastETag values.
        """
        byteReqHeaders = self.reqHeaders.copy()
        byteReqHeaders["Range"] = "bytes=%s-%s" % (self.lastLength, length)
        try:
            getResponse = self.connPool.urlopen(method="GET",
                                                url=self.url,
                                                headers=byteReqHeaders)
        except urllib3.connectionpool.MaxRetryError:
            print "Connection failed at %s" % datetime.now().strftime("%Y-%m-%d %I:%M %p")
            raise
        newData = getResponse.data
        # print new data
        sys.stdout.write(newData)
        sys.stdout.flush()
        # write data to file
        if self.outputFilePath:
            fileMode = "wb" if self.seenChanges is False else "ab"
            with open(self.outputFilePath, fileMode) as f:
                f.write(newData)
            self.seenChanges = True
        # reset "last" data
        self.lastLength = length
        self.lastETag = ETag

def main(logURL, server, logPatterns, username, password, pollingInterval, outputDir):
    # Handle different option cases
    if logURL and not server:
        logURLs = [logURL]
    elif not logURL and server:
        try:
            serverURL = SERVER_MAPPINGS[server]
        except KeyError:
            print "Given server name isn't a known shortcut. Trying the server name as a literal value..."
            serverURL = server
        print "Searching for logs matching patterns: %s" % logPatterns
        logURLs = get_log_filenames(serverURL, username, password, logPatterns)
        if not logURLs:
            raise ValueError, "No matching logfiles found"
    else:
        raise ValueError, "Unhandled case. Need to pass exactly one of server and logURL"

    # Create objects and store initial values
    logFileTailers = {}
    for logURL in logURLs:
        logFileTailers[logURL] = LogFileTailer(logURL, username, password, outputDir)
        logFileTailers[logURL].store_initial_length_and_etag()
    # Print info to console
    prettyDateTimeStart = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    print "Started monitoring at", prettyDateTimeStart
    print "***Content starts below this line***"
    # Main loop to tail files
    while True:
        try:
            for logFileTailer in logFileTailers.values():
                (length, ETag) = logFileTailer.check_for_changes()
                if length:
                    logFileTailer.download_and_output_new_data(length, ETag)
            time.sleep(pollingInterval)
        except KeyboardInterrupt:
            prettyDateTimeEnd = datetime.now().strftime("%Y-%m-%d %I:%M %p")
            sys.exit("\n Received keyboard interrupt at %s. Exiting..." % prettyDateTimeEnd)

if __name__ == "__main__":
    # # Option Parsing # #
    parser = OptionParser()
    parser.add_option("-u", "--url",
                    action="store",
                    default=None,
                    type="string",
                    dest="logURL",
                    help="The URL of the logfile to watch.")
    parser.add_option("-i", "--interval",
                    action="store",
                    default=2,
                    type="float",
                    dest="interval",
                    help="The polling interval in seconds. Default is %default.")
    parser.add_option("-d", "--directory",
                    action="store",
                    default=None,
                    type="string",
                    dest="outputDir",
                    help="Optionally specify a directory to write the data to.")
    parser.add_option("-s", "--server",
                    action="store",
                    default=None,
                    type="string",
                    dest="server",
                    help="URL of the server whose logfiles you want to watch.")
    parser.add_option("-p", "--patterns",
                    action="store",
                    default=DEFAULT_LOG_INCLUDE_PATTERNS,
                    type="string",
                    dest="logIncludePatterns",
                    help="comma separated list of logfile name patterns to include.")
    (options, args) = parser.parse_args()
    if not (options.logURL or options.server):
        parser.print_help()
        parser.error("You must provide either a logfile URL or a server")

    main(options.logURL,
        options.server,
        options.logIncludePatterns,
        LOG_USERNAME,
        LOG_PASSWORD,
        options.interval,
        options.outputDir)
