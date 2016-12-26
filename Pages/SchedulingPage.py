from common.common import Base, Main
from selenium.webdriver.common.by import By
from modals.AddEditShiftModal import ShiftModal
from modals.AutoScheduleModal import AutoScheduleModal
from modals.TemplatesModal import TemplatesModal
from modals.SettingsModal import SettingsModal
from modals.ConvertToHouseShiftModal import ConvertToHouseShift
from modals.LocationRotationModal import LocationRotationModal
from kpi_panel.KpiPanel import KpiPanelTabs
from modals.FilterModal import FilterModal
from modals.DeleteModal import DeleteModal
from datetime import datetime
import time
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException
import re

class SchedulingPage(Main):
    group_button = (By.CSS_SELECTOR, "span.group-label")
    calendar_btn = (By.CSS_SELECTOR, "button.ui-datepicker-trigger")
    group_dropdown = [(By.CSS_SELECTOR, "li.showNone.item"),
                     (By.CSS_SELECTOR, "li.showSchedule.item"),
                     (By.CSS_SELECTOR, "li.showLocation.item")]
    current_day = (By.CSS_SELECTOR, "th.currentDay")
    post = (By.CSS_SELECTOR, "button.post")
    post_badge = (By.CSS_SELECTOR, "button.primary.post span.post-count")
    name_sortable = (By.CSS_SELECTOR, "th.sortable employee-cell")
    employee_name = (By.CSS_SELECTOR, "td.employee-cell.sorting_2 div.employee-name[data-employee-id]")
    subheader = (By.CSS_SELECTOR, "div.subheader")
    filter_btn = (By.CSS_SELECTOR, "button.filterBtn")
    viewBy_btn = (By.CSS_SELECTOR, "div.btn-group")
    show_hide_btn = (By.CSS_SELECTOR, "li.show-hide-details")
    refresh_btn = (By.CSS_SELECTOR, "a.refreshScheduler")
    tools_dropdown = (By.CSS_SELECTOR, "a.tools-menu-button")
    expand_btn = (By.CSS_SELECTOR, "a.toggleScreen")
    this_week_button = (By.CSS_SELECTOR, "button.thisWeek.button.secondary")
    data_table = (By.CSS_SELECTOR, "dataTables_scrollBody")
    day_cells = (By.CSS_SELECTOR, "td.day-cell")
    employee_cell = (By.CSS_SELECTOR, "td.employee-cell")
    classic_view_btn = (By.CSS_SELECTOR, "div.btn-group a.button.secondary.first.selected")
    smart_view_btn = (By.CSS_SELECTOR, "div.btn-group a.button.secondary.second")
    kpi_panel = (By.CSS_SELECTOR, "div#scheduler-kpi")
    hide_details_option = (By.CSS_SELECTOR, "li.show-hide-details span.extra-details")
    show_details_option = (By.CSS_SELECTOR, "li.show-hide-details span.basic-details")
    inactive_employee_cell = (By.CSS_SELECTOR, "div.inactive")
    next_week_button = (By.CSS_SELECTOR, "a.next")
    previous_week_button = (By.CSS_SELECTOR, "a.prev")
    auto_schedule_menu_item = (By.CSS_SELECTOR, "div.dropdown-container li.item[data-tool='autoSchedule']")
    templates_menu_item = (By.CSS_SELECTOR, "div.dropdown-container li.item[data-tool='templates']")
    settings_menu_item = (By.CSS_SELECTOR, "div.dropdown-container li.item[data-tool=settings]")
    convert_to_house_shift_menu_item = (By.CSS_SELECTOR, "div.dropdown-container li.item[data-tool=convertHouseShifts]")
    location_rotation_menu_item = (By.CSS_SELECTOR, "div.dropdown-container li.item[data-tool=locationRotation]")
    delete_schedule_menu_item = (By.CSS_SELECTOR, "div.dropdown-container li.item[data-tool=deleteSchedule]")


    def __init__(self, driver, base_url, login, password):

        Main.__init__(self, driver, base_url, login, password)
        self.go(base_url + 'login.hs?username=%s&password=%s' % (login, password))
        self.wait_until_loading_dissapear()
        self.go(base_url + 'menuParser.hs?screen=newScheduling')
        self.wait_until_loading_dissapear()
        self.wait_until_loading_dissapear()
        self.close_walkme_popup()
        self.base_url = base_url
        self.login = login
        self.password = password

    def get_employee_day_for_schedule(self, schedule='', employee_id='', day_num=1):
        '''

        :param schedule: string schedule name
        :param employee_id: int employee id
        :param day_num: int number of the day in a buisness week
        :return: webelement
        '''

        locator = "//span[contains(text(),'{0}')]/ancestor::tbody/descendant::div[contains(@data-employee-id,'{1}')][1]/ancestor::tr[contains(@role, 'row')]/td[{2}]".format(schedule, employee_id, day_num+1)

        try:
            return self.find((By.XPATH, locator))
        except NoSuchElementException:
            return False

    def get_employee_day(self, employee_id='', day_num=1):
        """
        Work when grid is grouped by None
        return: By tuple
        """
        locator = "//div[contains(@data-employee-id, '{0}')]/ancestor-or-self::tr[contains(@role, 'row')]/td[{1}]".format(employee_id, day_num)
        return (By.XPATH, locator)

    def curr_date_compare(self, locale='En_gb'):
        # TODO Add support of different locale, rewrite for compare not only current date

        locale_format = {'En_gb': "%a, %m/%d/%y", 'En_us': '"%d/%m/%y"'}
        sched_c_date = time.strptime(self.get_element_text(self.current_day), locale_format[locale])

        curr_date = time.localtime(time.time())
        if curr_date.tm_mday == sched_c_date.tm_mday and curr_date.tm_mon == sched_c_date.tm_mon:
            return True
        else:
            return False


    def add_shift(self, day_num, employee_id):

        """
        self.wait_ajax_complete()
        script = "var event = new MouseEvent('dblclick', {view: window, bubbles: true, cancelable: true}); " \
                 "document.querySelector(\"div[data-employee-id=%s]\").parentElement.parentElement.parentElement.parentElement.getElementsByTagName(\'td\')[%d].dispatchEvent(event);" % (
                 employee_id, day_num + 1)
        """
        #self.driver.execute_async_script(script)
        return ShiftModal(self.driver, day_num, employee_id)

    def delete_shift(self, day_num, employee_id):
        self.wait_ajax_complete()
        script = "var event = new MouseEvent('click', {view: window, bubbles: true, cancelable: true}); " \
                 "document.querySelector(\"div[data-employee-id=%s]\").parentElement.parentElement.parentElement.parentElement.getElementsByTagName(\'td\')[%d].dispatchEvent(event);" % (
                 employee_id, day_num + 1)
        self.driver.execute_script(script)


    def get_previous_week(self):
        self.click(self.previous_week_button)
        self.wait_until_loading_dissapear()



    def get_next_week(self):
        self.click(self.next_week_button)
        self.wait_until_loading_dissapear()

    def get_autoscheduler(self):
        self.click(self.tools_dropdown)
        self.click(self.auto_schedule_menu_item)
        return AutoScheduleModal(self.driver)

    def get_url_date(self):

        url = self.driver.current_url
        pattern = re.compile("\\d{4}-\\d{2}-\\d{2}")
        url_date = pattern.search(url).string()

    def get_copy_schedule(self):
        # TODO
        pass

    def get_delete_schedule(self):
        # TODO
        self.get_settings()
        self.find(self.delete_schedule_menu_item).click()
        return DeleteModal(self.driver)

    def get_convertTo_house(self):
        self.find(self.tools_dropdown).click()
        self.find(self.convert_to_house_shift_menu_item).click()
        return ConvertToHouseShift(self.driver)

    def get_locationRotation(self):
        self.find(self.tools_dropdown).click()
        self.find(self.location_rotation_menu_item).click()
        return LocationRotationModal(self.driver)

    def get_templates(self):
        self.click(self.tools_dropdown)
        self.click(self.templates_menu_item)
        return TemplatesModal(self.driver)

    def get_unpost_schedule(self):
        # TODO
        pass

    def get_kpi(self):
        return KpiPanelTabs(self.driver)

    def get_settings(self):
        self.find(self.tools_dropdown).click()
        self.find(self.settings_menu_item).click()
        return SettingsModal(self.driver)

    def get_filters(self):
        self.click(self.filter_btn)
        return FilterModal(self.driver)









