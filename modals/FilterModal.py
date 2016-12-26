from selenium.webdriver.common.by import By
from modals.ModalsGeneral import ModalsElement


class FilterModal(ModalsElement):
    filter_btn = (By.CSS_SELECTOR, "button.filterBtn")
    filter_modal = (By.CSS_SELECTOR, "div.filterModal")
    filter_schedules_column = (By.CSS_SELECTOR, "td#schedules")
    filter_schedules_count = (By.CSS_SELECTOR, "td.filter-option.schedules span#schedules_count")
    filter_schedules_names = (By.CSS_SELECTOR, "td.filter-option.schedules span.filter_name")
    filter_job_column = (By.CSS_SELECTOR, "td.filter-option.jobs")
    filter_job_count = (By.CSS_SELECTOR, "td.filter-option.jobs span#jobs_count")
    filter_job_names = (By.CSS_SELECTOR, "td.filter-option.jobs span.filter_name")
    filter_locations_column = (By.CSS_SELECTOR, "td.filter-option.locations")
    filter_locations_count = (By.CSS_SELECTOR, "td.filter-option.locations span#locations_count")
    filter_locations_names = (By.CSS_SELECTOR, "td.filter-option.locations span.filter_name")
    filter_locations_nextPage = (By.CSS_SELECTOR, "td#locations span.nextPage")
    filter_locations_previousPage = (By.CSS_SELECTOR, "td#locations span.prevPage")


    filter_dayParts_column = (By.CSS_SELECTOR, "td.filter-option.dayParts")
    filter_dayParts_count = (By.CSS_SELECTOR, "td.filter-option.dayParts span#dayParts_count")
    filter_dayParts_names = (By.CSS_SELECTOR, "td.filter-option.dayParts span.dayParts_name")
    new_default_filters = (By.CSS_SELECTOR, "input.filter_defaults")
    hide_unscheduled_employee_option = (By.CSS_SELECTOR, "input#filter_unscheduled_0")
    button_apply = (By.CSS_SELECTOR, "button.primary[data-action=apply]")
    button_apply_disabled = (By.CSS_SELECTOR, "button.primary.disabled[data-action=apply]")
    clear_all_button = (By.CSS_SELECTOR, "a.button-link[data-action=clearAll]")

    schedules_more_sticky_filters = (By.CSS_SELECTOR, "td#schedules a.more-sticky-filters")
    jobs_more_sticky_filters = (By.CSS_SELECTOR, "td#jobs a.more-sticky-filters")
    locations_more_sticky_filters = (By.CSS_SELECTOR, "td#locations a.more-sticky-filters")

    schedules_less_sticky_filters = (By.CSS_SELECTOR, "td#schedules a.less-sticky-filters")
    jobs_less_sticky_filters = (By.CSS_SELECTOR, "td#schedules a.less-sticky-filters")
    locations_less_sticky_filters = (By.CSS_SELECTOR, "td#locations a.less-sticky-filters")

    save_as_new_default = (By.CSS_SELECTOR, "input.filter_defaults")
    filter_checkbox = "//td[@id='{0}']/descendant::span[text()='{1}']/preceding-sibling::input"

    schedules_sticky_filters_delimiter = (By.CSS_SELECTOR, "td#schedules div.stickyFilters")
    jobs_sticky_filters_delimiter = (By.CSS_SELECTOR, "td#jobs div.stickyFilters")
    locations_sticky_filters_delimiter = (By.CSS_SELECTOR, "td#locations div.stickyFilters")

    schedules_count = (By.CSS_SELECTOR, "span#schedules_count")
    jobs_count = (By.CSS_SELECTOR, "span#jobs_count")
    locations_count = (By.CSS_SELECTOR, "span#locations_count")
    dayParts_count = (By.CSS_SELECTOR, "span#dayParts_count")
    filter_btn = (By.CSS_SELECTOR, "button.filterBtn")
    def __init__(self, driver):
        self.driver = driver


    def open(self):
        self.click(self.filter_modal)


    def get_filter_names(self, filter_type):
        """
        :param filter_type: string Schedule, Job, Location, Day Part. Type of filter column from which need to get names Schedule, Job, Location, Day Part
        :return: array of names of selected column from filter pop-out
        """
        columns_names = {'Schedule': self.filter_schedules_names,
                         'Job': self.filter_job_names,
                         'Location': self.filter_locations_names,
                         'Day Part': self.filter_dayParts_names}


        schedules_name = self.find(columns_names[filter_type], True)
        names = []
        for element in schedules_name:
            names.append(self.get_element_text(element))

        return names
    def search(self, field, text):
        """

        :param field: name of field in what search
        :param text: search text
        :return: list of visible checkbox elements
        """
        pass

    @property
    def hide_unscheduled(self):
        """
        :return: filter modal with checked "Hide unscheduled employee checkbox
        """
        return self.click(self.hide_unscheduled)



    def set_schedule(self, schedule_name=''):
        """
        :param schedule_name: string Filter name as in filter modal
        :return:
        """
        locator = (By.XPATH, self.filter_checkbox.format('schedules', schedule_name))
        self.click(locator)

    def set_job(self, job_name=''):
        """

        :param job_name: string JobName
        :return: click to specific Job filter ckeckbox
        """
        locator = (By.XPATH, self.filter_checkbox.format('jobs', job_name))
        self.click(locator)


    def set_location(self, location_name=''):
        """

        :param location_name: strint location name
        :return: click to specific Location filter checkbox
        """

        locator = ((By.XPATH,  self.filter_checkbox.format('locations', location_name)))
        self.click(locator)

    def set_dayPart(self, dayPart_name=''):
        """

        :param dayPart_name:
        :return:
        """
        locator = (By.XPATH,  self.filter_checkbox.format('dayParts', dayPart_name))
        self.click(locator)

    def set_save_as_default(self):
        """
        :return: if save_as_new_default checkbox disabled : return False
        :return" if save_as_new_default_checkbox enabled : return click to save_as_new_default checkbox
        """

        if self.get_element_attribute(self.save_as_new_default, "disabled") == "disabled":
            return AttributeError
        else:
            self.click(self.save_as_new_default)

    def get_schedule(self, schedule_name=''):
        return self.find((By.XPATH, self.filter_checkbox.format('schedules', schedule_name)))

    def get_job(self, job_name=''):
        locator = (By.XPATH, self.filter_checkbox.format('jobs', job_name))
        return self.find(locator)


    def get_location(self, location_name):
        return self.find((By.XPATH, self.filter_checkbox.format('locations', location_name)))

    def get_dayPart(self, dayPart_name):
        self.find((By.XPATH, self.filter_checkbox.format('schedules', dayPart_name)))

    def get_schedules_count(self):
        """

        :return: int schedules count
        """
        return int(self.get_element_text(self.schedules_count))

    def get_jobs_count(self):
        """

        :return: int schedules count
        """
        return int(self.get_element_text(self.jobs_count))

    def get_locations_count(self):
        """

        :return: int locations count
        """
        return int(self.get_element_text(self.locations_count))

    def get_dayParts_count(self):
        """

        :return: int dayParts count
        """
        return int(self.get_element_text(self.dayParts_count))


    def apply(self):
        self.click(self.button_apply)

    def clear_all(self):
        self.click(self.clear_all_button)


    def save_as_default(self):
        """
        :return: filter modal with checked "Save as new default checkbox
        """
        self.save_as_default()
        self.apply()
