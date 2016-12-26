from selenium.webdriver.common.by import By
from modals.ModalsGeneral import ModalsElement


class UnpostModal(ModalsElement):
    unpost_modal_menu_item = (By.CSS_SELECTOR, "div.dropdown-container li.item[data-tool=unpostSchedule]")
    disable_unpost_modal_menu_item = (By.CSS_SELECTOR, "div.dropdown-container li.disabled.item[data-tool=unpostSchedule]")
    unpost_modal = (By.CSS_SELECTOR, "div.unpost-schedule-modal")
    button_unpost = (By.CSS_SELECTOR, "button.primary[data-action=unpost]")
    disable_button_unpost = (By.CSS_SELECTOR, "button.primary.disabled[data-action=unpost]")

    def select_schedule(self, schedule_name):
        pass


