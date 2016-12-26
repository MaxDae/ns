import pytest
from common.common import Base, Main
from selenium.webdriver.common.by import By
from modals.AddEditShiftModal import ShiftModal
import time


class SmartViewPage(Main):
    smart_view_btn = (By.CSS_SELECTOR, "a.button[data-week-view=smart]")
    sv_name_sortable = (By.CSS_SELECTOR, "div.sortButton.asc")
    week_button = (By.CSS_SELECTOR, "button.week.menuItem")
    day_button = (By.CSS_SELECTOR, "button.day.menuItem")
    employee_day_cell = (By.CSS_SELECTOR, "div.vis-group.employee-cell")
    unable_employee_time = (By.CSS_SELECTOR, "div.vis-item-overflow")
    shift_for_employee = (By.CSS_SELECTOR, "div.vis-item.vis-range.shift.vis-editable[data-shiftid]")
    job_for_shift = (By.CSS_SELECTOR, "div.vis-item-content div.job")
    location_for_shift = (By.CSS_SELECTOR, "div.vis-item-content div.location")
    tooltip_for_shift = (By.CSS_SELECTOR, "div.vis-item-content div.tooltip")
    





