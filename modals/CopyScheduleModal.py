import pytest
from selenium.webdriver.common.by import By
from modals.ModalsGeneral import ModalsElement

class CopyScheduleModal (ModalsElement):
    copy_schedule_menu_item = (By.CSS_SELECTOR, "div.dropdown-container li.item[data-tool=copySchedule]")
    copy_schedule_modal = (By.CSS_SELECTOR, "div.copy-schedule")
    calendar_picker_source_week = (By.CSS_SELECTOR, "button.ui-datepicker-trigger")
    calendar_picker_target_week = (By.CSS_SELECTOR, "button.ui-datepicker-trigger")
    open_data_picker = (By.CSS_SELECTOR, "div#ui-datepicker-div")
    button_copy = (By.CSS_SELECTOR, "a.button.primary[data-action=copy]")
    disable_button_copy = (By.CSS_SELECTOR, "a.button.primary.disabled[data-action=copy]")



