import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_located_to_be_selected
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.common.exceptions import *
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys



class Base(object):

    @pytest.fixture(scope="class", autouse=True)
    def manage_driver(self, request, driver):

        driver.start()
        request.addfinalizer(driver.stop)

class Element(object):

    def __get__(self, instance):
        driver =  instance.driver



class Main(Element):

    schedules = (By.XPATH, "id('nav-area')//span[contains(text(),'schedules')]")
    scheduling = (By.XPATH, "id('nav-area')//span[contains(text(),'scheduling')]")
    no_button = (By.ID, "Buitit")
    loadingScreen = (By.CSS_SELECTOR, "div#hs-LoadingAnimation")
    walkme_menu = (By.CSS_SELECTOR, "div.walkme-action-close")


    def __init__(self, driver, base_url, login, password):
        self.driver = driver.instance
        #self.go(base_url + 'login.hs?username=%s&password=%s' % (login, password))
        #self.wait_until_loading_dissapear()


    def wait_ajax_complete(self):


        WebDriverWait(self.driver, 2000).until(lambda d: d.execute_script("return jQuery.active == 0") )



    def go(self, url):
        """
        :param url:
        :return:
        """
        return self.driver.get(url)

    def login_by_url(self, base_url, login, password):
        '''
        login: login for login
        password: password for login
        return: page with appointed credentials
        '''

        return self.go(base_url+'login.hs?username=%s&password=%s'%(login, password))

    def find(self, locator, elements=None):
        """
        locator: tuple, CSS or XPATH locator in (By, locator) format
        elements: default None
        elements: if NOT None return list of WebElements according to find_elements
        return: WebElement OR list of WebElements
        """
        if isinstance(locator, WebElement):
            return locator
        else:

            if elements is not None:
                try:
                    return self.driver.find_elements(*locator)
                except ElementNotVisibleException:
                    WebDriverWait(self.driver, 1000).until(lambda s: self.is_element_present(locator))

            else:
                try:
                    return self.driver.find_element(*locator)
                except ElementNotVisibleException or StaleElementReferenceException:
                    WebDriverWait(self.driver, 1000).until(lambda s: self.is_element_present(locator))


    def is_element_selected(self, locator):
        if  isinstance(locator, WebElement):



            if locator.is_selected() or locator.get_attribute('checked') is not None:
                return True
            else:
                return False
        else:
            if self.find(locator).is_selected() or self.find(locator).get_attribute('checked') is not None:
                return True
            else:
                return False


    def is_element_present(self, *locator):
        self.driver.implicitly_wait(0)
        """
        if  isinstance(locator, tuple) and isinstance(locator[0], WebElement):
            if locator[0].is_displayed():
                return True
        else:
        """
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            self.driver.implicitly_wait(10)


    def wait_until_loading_dissapear(self):
        try:
            WebDriverWait(self.driver, 1000).until(lambda s: not self.is_element_present(self.loadingScreen))
        except TimeoutException:
            self.driver.refresh()

    def get_element_text(self, element):
        if isinstance(element, WebElement):
            return element.text
        else:
            return self.find(element).text

    def get_element_attribute(self, locator, attribute):
        return self.find(locator).get_attribute(attribute)

    def close_walkme_popup(self):
         try:
             self.find(self.walkme_menu).click()

         except NoSuchElementException or ElementNotVisibleException or AttributeError:
             pass

    def click(self, element):
        try:
            return self.find(element).click()
        except ElementNotSelectableException or StaleElementReferenceException:
            WebDriverWait(self.driver, 1000).until(lambda s: EC.element_to_be_clickable(element))
        except NoSuchElementException:
            return NoSuchElementException

    def dbl_click(self, webelement):
        action = AC(self.driver)
        return action.double_click(webelement).perform()

    def send_text(self, locator, text):
        """
        locator: tuple, CSS or XPATH locator in (By, locator) format
        elements: default None

        """
        return self.click(locator).send_keys(text)

    def ctrl_V(self, locator):
        '''

        :param locator: locator in By. tuple format
        :param keys: Keys object parameter
        :additional_key: Some key "c" OR "v"
        :return:
        '''
        element = self.find(locator)
        action = AC(self.driver)
        action.move_to_element(element).click(element).send_keys(Keys.CONTROL+"v").perform()


    def ctrl_C(self, locator):
        element = self.find(locator)
        action = AC(self.driver)
        action.move_to_element(element).click(element).send_keys(Keys.CONTROL+"c").perform()

    def ctrl_X(self, locator):
        element = self.find(locator)
        action = AC(self.driver)
        action.move_to_element(element).click(element).send_keys(Keys.CONTROL+"x").perform()

    def ctrl_Z(self, locator):
        element = self.find(locator)
        action = AC(self.driver)
        action.move_to_element(element).click(element).send_keys(Keys.CONTROL+"z").perform()

    def ctrl_Y(self, locator):
        element = self.find(locator)
        action = AC(self.driver)
        action.move_to_element(element).click(element).send_keys(Keys.CONTROL+"y").perform()

    def ctrl_T(self, locator):
        element = self.find(locator)
        action = AC(self.driver)
        action.move_to_element(element).click(element).send_keys(Keys.CONTROL+"t").perform()

    def DELETE_button(self, locator):
        element = self.find(locator)
        action = AC(self.driver)
        action.move_to_element(element).click(element).send_keys(Keys.DELETE).perform()












