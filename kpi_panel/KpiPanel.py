
from common.common import Base, Main
from selenium.webdriver.common.by import By


class KpiPanelTabs(Main):
    # KPI Tabs
    house_shift_tab = (By.CSS_SELECTOR, "a[data-tab=house-shift-manager]")
    schedule_summary_tab = (By.CSS_SELECTOR, "a[data-tab=schedule-summary]")
    forecast_data_tab = (By.CSS_SELECTOR, "a[data-tab=forecast-data]")
    labor_budget_tab = (By.CSS_SELECTOR, "a[data-tab=labor-budget]")
    labor_volume_tab = (By.CSS_SELECTOR, "a[data-tab=labor volume]")

    # House Shift Manager tab
    house_shift_badge_count = (By.CSS_SELECTOR, "span.house-shift-count")
    day_with_house_shift = (By.CSS_SELECTOR, "div.daily-house-shifts")
    day_label = (By.CSS_SELECTOR, "div.hr-label")
    house_shift = (By.CSS_SELECTOR, "div.house.shift.ui-draggable.ui-draggable-handle[data-id]")
    house_shift_job = (By.CSS_SELECTOR, "div.job.text-house-shift")
    house_shift_location = (By.CSS_SELECTOR, "div.location.text-house-shift")
    start_time_of_house_shift = (By.CSS_SELECTOR, "span.text-nowrap.text-house-shift")
    out_time_of_house_shift = (By.CSS_SELECTOR, "span.outTime.text-nowrap.text-house-shift")

    # Schedule Summary tab
    toggle_summary_table = (By.CSS_SELECTOR, "a.button.secondary.first.scheduleSummaryTable")
    toggle_summary_chart = (By.CSS_SELECTOR, "a.button.secondary.second.scheduleSummaryChart")
    total_shifts_label = (By.CSS_SELECTOR, "tr[data-id=shifts]")
    shifts_weekly_total = (By.CSS_SELECTOR, "tr[data-id=shifts] span.weeklyTotal")
    total_hours_label = (By.CSS_SELECTOR, "tr[data-id=hours]")
    hours_weekly_total = (By.CSS_SELECTOR, "tr[data-id=hours] span.weeklyTotal")
    total_cost_label = (By.CSS_SELECTOR, "tr[data-id=cost]")
    cost_weekly_total = (By.CSS_SELECTOR, "tr[data-id=cost] span.weeklyTotal")
    summary_chart = (By.CSS_SELECTOR, "div#scheduler-kpi div.highcharts-container")

    # Forecast Data tab
    volume_type = (By.CSS_SELECTOR, "td.volumeHeader")

    # Labor Budget
    labor_budget_type = (By.CSS_SELECTOR, "select.labor-budget-type")
    labor_dollars = (By.CSS_SELECTOR, "option[value='0']")
    labor_percent = (By.CSS_SELECTOR, "option[value='1']")
    labor_splh = (By.CSS_SELECTOR, "option[value='2']")
    labor_gplh = (By.CSS_SELECTOR, "option[value='3']")
    labor_lh100 = (By.CSS_SELECTOR, "option[value='4']")
    labor_hours = (By.CSS_SELECTOR, "option[value='5']")
    labor_total = (By.CSS_SELECTOR, "td[data-collapse-toggle=labor-total]")

    # Labor Volume
    labor_volume_table_view = (By.CSS_SELECTOR, "a.table-switch")
    labor_volume_graph_view = (By.CSS_SELECTOR, "a.chart-switch")
    forecast_labor_volume = (By.CSS_SELECTOR, "td[data-collapse-toggle=forecast]")
    scheduled_labor_volume = (By.CSS_SELECTOR, "td[data-collapse-toggle=schedule]")
    optimal_labor_volume = (By.CSS_SELECTOR, "td[data-collapse-toggle=optimal]")
    actual_labor_volume = (By.CSS_SELECTOR, "td[data-collapse-toggle=actual]")

    def __init__(self, driver):
       self.driver = driver

    def get_hs_manager(self):
        return self.click(self.house_shift_tab)

    def get_labor_budget(self):
        self.click(self.labor_budget_tab)

    def get_schedule_suummary(self):
        self.click(self.schedule_summary_tab)

    def get_forecast_data(self):
        self.click(self.forecast_data_tab)

    def get_labor_volume(self):
        self.click(self.labor_volume_tab)

    def get_chart_view(self):
        self.click(self.chart_switch)

    def get_table_view(self):
        self.click(self.table_switch)


