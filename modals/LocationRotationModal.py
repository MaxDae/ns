
from selenium.webdriver.common.by import By
from modals.ModalsGeneral import ModalsElement


class LocationRotationModal(ModalsElement):
    location_rotation_menu_item = (By.CSS_SELECTOR, "div.dropdown-container li.item[data-tool=locationRotation]")
    disable_location_rotation_menu_item = (By.CSS_SELECTOR, "div.dropdown-container li.disabled[data-tool=locationRotation]")
    location_rotation_modal = (By.CSS_SELECTOR, "div.location-rotation-modal")
    rotate_start_time_checkbox = (By.CSS_SELECTOR, "input.rotateStartTime")
    rotate_button = (By.CSS_SELECTOR, "button.primary[data-action=rotate]")
    disabled_rotate_button = (By.CSS_SELECTOR, "button.primary.disabled[data-action=rotate]")
    location_rotation_modal = (By.XPATH, "//span[text()='Location Rotation']/ancestor::div[@role='dialog']")

    def __init__(self, driver):
        self.driver = driver

    def select_schedule(self, schedule_id):
        '''
        :param schedule_id:
        :return: click to radio button webelement for specific schedule
        '''
        schedule = list(self.select_one)
        schedule[1] = self.select_one[1].format(schedule_id)
        return self.find(tuple(schedule)).click()

    def rotate_location(self):
        return self.find(self.rotate_button).click()
