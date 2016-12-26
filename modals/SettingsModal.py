
from selenium.webdriver.common.by import By
from modals.ModalsGeneral import ModalsElement


class SettingsModal (ModalsElement):

    settings_modal = (By.CSS_SELECTOR, "div.display-settings")
    preferred_name_setting = (By.NAME, "preferedName")
    out_time_setting = (By.CSS_SELECTOR, "div.checkbox input[name=outTime]")
    job_setting = (By.CSS_SELECTOR, "div.checkbox input[name=job]")
    location_setting = (By.CSS_SELECTOR, "div.checkbox input[name=location]")
    house_shift_manager_setting = (By.CSS_SELECTOR, "div.checkbox input[name=houseShiftManager]")
    schedule_summary_setting = (By.CSS_SELECTOR, "div.checkbox input[name=scheduleSummary]")
    schedule_violations_setting = (By.CSS_SELECTOR, "div.checkbox input[name=forecastComparison]")
    forecast_data_setting = (By.NAME, "forecastData")
    labor_budget_setting = (By.CSS_SELECTOR, "div.checkbox input[name=budgetComparison]")
    labor_forecast_setting = (By.CSS_SELECTOR, "div.checkbox input[name=forecastComparison]")
    minor_alert_setting = (By.CSS_SELECTOR, "div.checkbox input[name=minor]")
    availability_alert_setting = (By.CSS_SELECTOR, "div.checkbox input[name=availability]")
    overtime_alert_setting = (By.CSS_SELECTOR, "div.checkbox input[name=overtime]")
    aca_setting = (By.NAME, "aca")
    view_schedule_by_setting = (By.CSS_SELECTOR, "div.dropDown[data-id=viewScheduleBy]")
    default_shift_length_setting = (By.CSS_SELECTOR, "div.checkbox[data-id=maxShiftLength] input.twoDigitSize")
    sort_smartSelect_by_setting = (By.CSS_SELECTOR, "div.dropDown[data-id=sortSmartSelectBy]")
    button_save = (By.CSS_SELECTOR, "button.primary[data-action=save]")
    button_save_disabled = (By.CSS_SELECTOR, "button.primary.disabled[data-action=save]")
    tools_dropdown = (By.CSS_SELECTOR, "a.tools-menu-button")
    settings_menu_item = (By.CSS_SELECTOR, "div.dropdown-container li.item[data-tool=settings]")

    def __init__(self, driver):
        self.driver = driver

    def save_settings(self):
        self.click(self.button_save)

    def get_settings(self):
        self.find(self.tools_dropdown).click()
        self.find(self.settings_menu_item).click()
