import pytest
from selenium.webdriver.common.by import By
from common.common import Main
from selenium.webdriver.common.action_chains import ActionChains
from modals.ModalsGeneral import ModalsElement
from selenium.common.exceptions import NoSuchElementException


class ShiftModal(ModalsElement):
    shift_modal = (By.CSS_SELECTOR, "div.day-editor")
    add_shift_modal_title = (By.CSS_SELECTOR, "div.header.ui-draggable-handle")
    edit_shift_modal_title = (By.CSS_SELECTOR, "div.header.ui-draggable-handle")
    shift_modal_firstname = (By.CSS_SELECTOR, "div.header.ui-draggable-handle span.firstname")
    shift_modal_lastname = (By.CSS_SELECTOR, "div.header.ui-draggable-handle span.lastname")
    shift_modal_preferedname = (By.CSS_SELECTOR, "div.header.ui-draggable-handle span.preferedname")
    shift_modal_close = (By.CSS_SELECTOR, "button.ui-dialog-titlebar-close.close")
    shift_modal_start_time = (By.CSS_SELECTOR, "div.shift-editor input.start-time.input-sm.form-control")
    shift_modal_end_time = (By.CSS_SELECTOR, "div.shift-editor input.end-time.input-sm.form-control")
    shift_modal_job = (By.CSS_SELECTOR, "div.shift-editor select.jobComboBox")
    shift_modal_location = (By.CSS_SELECTOR, "div.shift-editor select.locationComboBox")
    shift_modal_duration_per_shift = (By.CSS_SELECTOR, "div.shift-editor span.duration")
    shift_modal_cost_per_shift = (By.CSS_SELECTOR, "div.shift-editor span.cost")
    shift_modal_total_per_day_duration = (By.CSS_SELECTOR, "span.day-total-hours")
    shift_modal_total_per_day_cost = (By.CSS_SELECTOR, "div.footer span.day-total-cost")
    shift_modal_another_shift = (By.CSS_SELECTOR, "a.add-another-shift")
    shift_modal_save = (By.CSS_SELECTOR, "button.save")
    shift_modal_cancel = (By.CSS_SELECTOR, "a.close.button.link")
    shift_modal_delete = (By.CSS_SELECTOR, "a.delete.button.link")
    shift_modal_delete_icon = (By.CSS_SELECTOR, "a.delete>i.ico")
    shift_modal_error_message = (By.CSS_SELECTOR, "div.shift-editor span.error-message")
    shift_modal_start_time_error = (By.CSS_SELECTOR, "div.shift-editor input.start-time.input-sm.form-control.error")
    shift_modal_start_end_error = (By.CSS_SELECTOR, "div.shift-editor input.end-time.input-sm.form-control.error")
    shift_modal_read_only_mode = (By.CSS_SELECTOR, "div.day-editor.read-only")
    shift_modal_timeline = (By.CSS_SELECTOR, "div.vis-timeline")
    shift_modal_timeline_content = (By.CSS_SELECTOR, "div.vis-item-content div.job")
    shift_modal_timeline_tooltip = (By.CSS_SELECTOR, "div.vis-item-content div.tooltip")
    no_such_element = (By.CSS_SELECTOR, "div.olol")

    def __init__(self, driver, day_num = 0, employee_id = 0 ):
        self.driver = driver
        self.wait_ajax_complete()
        script = "var event = new MouseEvent('dblclick', {view: window, bubbles: true, cancelable: true}); " \
            "document.querySelector(\"div[data-employee-id=%s]\").parentElement.parentElement.parentElement.getElementsByTagName(\'td\')[%d].dispatchEvent(event);" % (employee_id, day_num + 1)
        self.driver.execute_script(script)






    def fill (self, start_time, end_time, job, location):
        self.find(self.shift_modal_start_time).click()
        self.find(self.shift_modal_start_time).send_keys(start_time)
        self.find(self.shift_modal_end_time).click()
        self.find(self.shift_modal_end_time).send_keys(end_time)
        job_option = self.find(self.shift_modal_job, True)
        location_option = self.find(self.shift_modal_location, True)
        action = ActionChains(self.driver)



        for element in job_option:
            if element.text == job:
                action.click(element)
        for element in location_option:
            if element.text == location:
                action.click(element)

    def save(self):
        self.find(self.shift_modal_save).click()

    def delete_shift (self):
        # TODO Add ability to select what shift should be deleted when several shifts in a modal

        return self.find(self.shift_modal_delete).click()

    def get_total_per_shift(self):
        return float(self.get_element_text(self.shift_modal_duration_per_shift))

    def get_total_per_day(self):
       return float(self.get_element_text(self.shift_modal_total_per_day_duration))

    def get_full_name(self):
        #TODO rewrite for support prefered name if user choose this option
        full_name = '{} {}'.format(self.get_element_text(self.shift_modal_firstname), self.get_element_text(self.shift_modal_lastname))
        return full_name












