
from selenium.webdriver.common.by import By
from common.common import Main
from modals.ModalsGeneral import ModalsElement


class DeleteModal(ModalsElement):
    delete_modal_menu_item = (By.CSS_SELECTOR, "div.dropdown-container li.item[data-tool=deleteSchedule]")
    disable_delete_modal_menu_item = (By.CSS_SELECTOR, "div.dropdown-container li.disabled.item[data-tool=deleteSchedule]")
    delete_schedule_modal = (By.CSS_SELECTOR, "div.delete-schedule-modal")
    button_delete = (By.CSS_SELECTOR, "button.primary[data-action=delete]")
    disable_button_delete = (By.CSS_SELECTOR, "button.primary.disabled[data-action=delete]")
    schedule_checkbox = (By.XPATH, "//div[@class='checkbox']/descendant::span[contains(text(), '{0}')]")

    def __init__(self, driver):
        self.driver = driver

    def delete_schedule(self, schedule_name):
        sc = list(self.schedule_checkbox)
        sc[1] = self.schedule_checkbox[1].format(schedule_name)
        self.click(tuple(sc))
        return self.click(self.button_delete)

