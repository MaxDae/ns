from selenium.webdriver.common.by import By

from common.common import Main

class ModalsElement(Main):
    modal_window = (By.CSS_SELECTOR, "div.ui-dialog-content.ui-widget-content")
    modal_title = (By.CSS_SELECTOR, "div.ui-dialog-titlebar")
    modal_close_button = (By.CSS_SELECTOR, "button.ui-dialog-titlebar-close")
    modal_cancel_button = (By.CSS_SELECTOR, "a[data-action=cancel]")
    loading_screen = (By.CSS_SELECTOR, "div#hs-LoadingAnimation")
    modal_bottom_message = (By.CSS_SELECTOR, "div#alert-save>span")
    disable_screen = (By.CSS_SELECTOR, "div#blockingOverlay")
    select_all = (By.CSS_SELECTOR, "div.checkbox input[data-action=selectAll]")
    select_one = (By.CSS_SELECTOR, "div.checkbox input.filterOption")
    confirmation_message_title = (By.CSS_SELECTOR, "div.body p.boldTitle")   # for unpost and delete schedule modals
    confirmation_message_button_yes = (By.CSS_SELECTOR, "a.button.primary[data-action=yes]")

    def __init__(self, driver):
        self.driver = driver

    def close(self):
        self.find(self.modal_close_button).click()

    def cancel(self):
        self.find(self.modal_cancel_button).click()

    def get_title(self):
        return self.get_element_text(self.modal_title)

    def select_all_checkbox(self):
        return self.find(self.select_all).click()

    def select_one_checkbox(self):
        return self.find(self.select_one).click()

    def fill(self, *args, **kwargs):
        pass




