import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, InvalidSwitchToTargetException, NoAlertPresentException
#from API.employee_info import clientData
import os
import json


from operator import contains, eq
#from browsermobproxy import Server

import ConfigParser
conf = ConfigParser.ConfigParser()
conf.read('pytest.ini')
configs = conf.sections()





#server = Server(pytest.config.getini('proxy_path'))



base_url = 'http://206.127.17.228/hs/'
base_timeout = 3000

urls = {
        'beta': 'http://216.166.0.39/hs/',
        'beta2': 'http://216.166.0.216/hs/',
        'staging': 'http://206.127.17.227/hs/',
        'df1': 'http://df-testserver1/hs/',
	    'df2': 'http://df-testserver2/hs/',
	    'df3': 'http://206.127.17.228/hs/',
        'df4': 'http://216.166.0.49/hs/',
        'df5': 'http://df-testserver5/hs/',

	     }
fp = webdriver.FirefoxProfile()

BROWSERS = {
          'ff': DesiredCapabilities.FIREFOX,
          'chrome': DesiredCapabilities.CHROME,
          'ie': DesiredCapabilities.INTERNETEXPLORER,
  } 
seleniumServerHost = "http://127.0.0.1"
seleniumServerPort = "4444"

# End of general config section

#Py.Test fixtures 


def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "ff", help = "Browser: ff, chrome or ie")
    parser.addoption("--base_url", action = "store", default = 'df3', help = 'Default testserver url df3 or df4')
    parser.addoption("--proxy", action = "store", default = 'No', help = 'Yes: use proxy, No: without proxy')

def pytest_configure(config):
    browser = config.getoption('browser')
    #config.getini('proxy_path')
    config.browser = BROWSERS[browser]
    config.timeout = base_timeout




@pytest.fixture(scope="class")
def browser(request):
    return request.config.get_option("--browser")



@pytest.fixture(scope="class")
def base_url(request):

    url = request.config.option.base_url
    if url in urls.keys():
       return urls[url]
    else:
      return base_url

@pytest.fixture(scope="class")
def resource(request):
    env = next(x for x in os.environ['PYTHONPATH'].split(';') if 'new_scheduler_tests' in x)

    if 'nt' in os.name:
        res = os.path.join(env, '\\recources\\')
    elif "nix" in os.name:
        res = os.path.join(env, '/recources/'+metafunc.cls+".json")
        try:
            with open(res) as recources:
                recources = json.load(recources)
                for k, v in recources:
                    metafunc.parametrize(k, v)
        except IOError as io:
            print io.message
            print "File not found %s".format(io.filename)










"""
@pytest.fixture(scope="class")
def jobLocationMap(request):
    if request.cls:
        res = os.path.dirname(os.path.realpath(__file__))

        jl_map = clientData(base_url, user, passw)
    return jl_map.getJobsLocation()
"""

class DB():
    pass

"""
@pytest.fixture(scope="session")
def db_connect(app, request):
    try:
        from sqlalchemy.dialects.mssql import base, pyodbc, adodbapi, pymssql, zxjdbc, mxodbc, pypyodbc

    except ImportError as e:
        print e.message
        print "You need to install SQLAlchemy"
    #cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DFQASQLVN01;DATABASE=HSV32MAIN;UID=hs;PWD=topgun')
"""




class DriverManager(object):

    # TODO Rewrite for support multithreading
    # TODO Add correct support of Save modal closing

    def __init__(self):
        self._instance = None

    def start(self, br='ff'):
        """
        server.start()
        proxy = server.create_proxy()

        if pytest.config.browser == 'ff':
            drv = pytest.config.browser['proxy']={
                "httpProxy": proxy.proxy,
                "ftpProxy": proxy.proxy,
                "sslProxy": proxy.proxy,
                "noProxy": None,
                "proxyType": "MANUAL",
                "autodetect": False


            }
        else:
            drv = pytest.config.browser
        """
        drv = pytest.config.browser

        self._instance = webdriver.Remote(command_executor='%s:%s/wd/hub' % (seleniumServerHost, seleniumServerPort), 
        	desired_capabilities = drv)
        self._instance.implicitly_wait(base_timeout)

        return self._instance

    @property
    def instance(self):
        if not self._instance:
            self.start()
        return self._instance

    def stop(self):
        self._instance.close()
        if EC.alert_is_present():
            try:

                WebDriverWait(self._instance, 3).until(EC.alert_is_present(),'Timed out waiting for PA creation ')
                alert = self._instance.switch_to_alert()
                alert.accept()
                #elif not EC.alert_is_present():
                self._instance.close()

            except Exception:
                pass
            except InvalidSwitchToTargetException:
                pass
            except NoAlertPresentException:
                pass
            except TimeoutException:
                pass
        else:
            pass


@pytest.fixture(scope="class")
def driver():
    return DriverManager()


