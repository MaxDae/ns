
from selenium.webdriver.common.by import By
from modals.ModalsGeneral import ModalsElement


class ConvertToHouseShift (ModalsElement):
    convert_to_house_shift_menu_item = (By.CSS_SELECTOR, "div.dropdown-container li.item[data-tool=convertHouseShifts]")
    disable_convert_to_house_shift_menu_item = (By.CSS_SELECTOR,
                                                "div.dropdown-container li.disabled.item[data-tool=convertHouseShifts])")
    convert_to_house_shift_modal = (By.CSS_SELECTOR, "div.ui-dialog.convert-to-house-modal")
    button_ok = (By.CSS_SELECTOR, "button.primary[data-action=ok]")
    button_ok_disabled = (By.CSS_SELECTOR, "button.primary.disabled[data-action=ok]")
    convert_to_house_shift_modal = (By.XPATH, "//span[text()='Convert to House Shifts']/ancestor::div[@role='dialog']")

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

    def convert_action(self):
        return self.find(self.button_ok).click()


