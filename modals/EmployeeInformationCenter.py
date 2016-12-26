from selenium.webdriver.common.by import By

from modals.ModalsGeneral import ModalsElement

class EIC(ModalsElement):

    employee_name = (By.CSS_SELECTOR, "div[data-employee-id={0}]")
    employee_info_popout = (By.CSS_SELECTOR, "div.employee-info-center")
    employee_info_popout_firstname = (By.CSS_SELECTOR, "div.employee-info-center span.firstname")
    employee_info_popout_lastname = (By.CSS_SELECTOR, "div.employee-info-centerspan.lastname")
    employee_info_popout_preferedname = (By.CSS_SELECTOR, "div.employee-info-center span.preferedname")
    employee_info_general_tab = (By.CSS_SELECTOR, "div.employee-info-center a.button-link[data-tab=general]")
    employee_avatar = (By.CSS_SELECTOR, "div.employee-info-general div.avatar>img")
    employee_phone = (By.CSS_SELECTOR, "div.employee-info-general div.phone")
    send_message_button = (By.CSS_SELECTOR, "div.employee-info-general button.sendMessage")
    employee_info_certifications = (
        By.CSS_SELECTOR, "div.employee-info-general div.certifications table#ee-certifications td.sorting_1")
    employee_info_availability_tab = (By.CSS_SELECTOR, "div.employee-info-center a.button-link[data-tab=availability]")
    employee_availability_table = (By.CSS_SELECTOR, "div.employee-info-center div.employee-info-availability")
    employee_info_jobs_tab = (By.CSS_SELECTOR, "div.employee-info-center a.button-link[data-tab=jobs]")
    employee_jobs_table = (By.CSS_SELECTOR, "div.employee-info-center div.employee-info-jobs")

    def __init__(self, driver, base_url, login, password, employee_id):
        ModalsElement.__init__(self, driver, base_url, login, password)
        employee_name = list(self.employee_name)
        employee_name[1] = self.employee_name[1].format(employee_id)
        self.find(tuple(employee_name)).click()

