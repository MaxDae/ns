import pytest
from selenium.webdriver.common.by import By
from modals.ModalsGeneral import ModalsElement


class AutoScheduleModal(ModalsElement):
    auto_schedule_menu_item = (By.CSS_SELECTOR, "div.dropdown-container li.item[data-tool='autoSchedule']")
    disabled_auto_schedule_menu_item = (By.CSS_SELECTOR, "div.dropdown-container li.disabled.item[data-tool='autoSchedule'])")
    auto_schedule_modal = (By.CSS_SELECTOR, "div.auto-schedule")
    generate_schedule_button = (By.CSS_SELECTOR, "button.primary[data-action='generateSchedule']")
    disable_generate_schedule_button = (By.CSS_SELECTOR, "button.primary.disabled[data-action='generateSchedule']")
    schedule_name_checkbox = (By.CSS_SELECTOR, "div.checkbox input[name='scheduleId']")
    schedule_name_checkbox_disable = (By.CSS_SELECTOR, "span.disabledFilter")
    select_auto_schedule_settings = (By.CSS_SELECTOR, "div.settings-group")
    auto_schedule_house_shift = (By.CSS_SELECTOR, "div.checkbox input[name='autoHouse']")
    auto_schedule_assigned_shifts = (By.CSS_SELECTOR, "div.checkbox input[name='autoRegular']")
    allow_employee_multiple_shifts = (By.CSS_SELECTOR, "div.checkbox input[name='allowMultipleShifts']")
    schedule_shifts_on_unavailable_day = (By.CSS_SELECTOR, "div.checkbox input[name='allowUnavailableShifts']")
    honor_request_off_option = (By.CSS_SELECTOR, "div.checkbox input[name='honorRequestOff']")
    use_location_limits_per_work_week =(By.CSS_SELECTOR, "div.checkbox input[name='limitLocation']")
    aca_hours_limits = (By.CSS_SELECTOR, "div.checkbox input[name='useHourLimits']")
    no_skill_level_rule = (By.CSS_SELECTOR, "div.checkbox input[name=skillLevel][value='0']")
    use_skill_level_rule = (By.CSS_SELECTOR, "div.checkbox input[name=skillLevel][value='1']")
    use_location_skill_levels = (By.CSS_SELECTOR, "div.checkbox input[name=skillLevel][value='2']")
    max_allowable_hours_input_field = (By.CSS_SELECTOR, "input[name=maxHours]")
    max_allowable_days_input_field = (By.CSS_SELECTOR, "input[name=maxDays]")
    schedule_radio_btn = (By.XPATH, "//input[@value='{0}']")

    def __init__(self, driver):
        self.driver = driver


    def select_schedule(self, schedule_id):
        '''
        :param schedule_id:
        :return: click to radio button webelement for specific schedule
        '''
        schedule = list(self.schedule_radio_btn)
        schedule[1] = self.schedule_radio_btn[1].format(schedule_id)
        return self.find(tuple(schedule)).click()

    def fill_max_hours(self, hours):
        return self.find(self.max_allowable_hours_input_field).click().send_keys(hours)

    def select_skill_level(self, skill_lvl):
        pass


    def generate(self):
        return self.find(self.generate_schedule_button).click()




