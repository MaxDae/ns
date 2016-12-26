import datetime
import time
import urllib2

f = open('rest_log.txt', 'a')
url = ''
sleepSeconds = 300
expectedString = '<token>'

def connection_test():

    # Write TimeStamp. CST = UTC - 5hours
    cstTime = datetime.datetime.utcnow() - datetime.timedelta(hours=5)
    cstTimeStr = str(cstTime)
    f.write('---------------------------\n')
    f.write(cstTimeStr + '\n')

    authData = None
    # Start Timing
    start = time.time()
    # REST Call
    try:
        authData = urllib2.urlopen(url).read()
    except Exception, e:
        errorStr = str(e)
        print errorStr
        f.write(errorStr + '\n')
    # Stop Timing
    latencyMS = (time.time() - start) * 1000

    if authData is not None:
        if expectedString in authData:
            print 'OK'
            f.write('OK\n')
        else:
            print '%s not found in response'  % expectedString
            f.write('%s not found in response' % expectedString)

    f.write('%i MS\n' % latencyMS)

while True:
    connection_test()
    time.sleep(sleepSeconds)
