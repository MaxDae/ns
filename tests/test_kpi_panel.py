import pytest
from common.common import Base
from Pages.SchedulingPage import SchedulingPage

@pytest.mark.parametrize(("username", "password"), [("autoTestUser", "testpassword123")])
class TestKpiPanel(Base):
    def test_kpi_panel_elements(self, driver, base_url, username, password):
        panel = SchedulingPage(driver, base_url, username, password).get_kpi()
        # verify elements on House Shift Manager tab
        assert panel.find(panel.house_shift_tab)
        panel.click(panel.house_shift_tab)

        # verify elements on Schedule Summary tab
        assert panel.find(panel.schedule_summary_tab)
        panel.get_schedule_suummary()
        assert panel.find(panel.toggle_summary_table)
        assert panel.find(panel.total_shifts_label)
        assert panel.find(panel.total_hours_label)
        assert panel.find(panel.total_cost_label)
        assert panel.find(panel.cost_weekly_total)
        panel.click(panel.toggle_summary_chart)
        assert panel.find(panel.summary_chart)

        # verify elements on Schedule Violations tab
        assert panel.find(panel.forecast_data_tab)

        # verify elements on Labor Budget tab
        assert panel.find(panel.labor_budget_tab)
        panel.click(panel.labor_budget_type)
        assert panel.find(panel.labor_dollars)
        assert panel.find(panel.labor_percent)
        assert panel.find(panel.labor_splh)
        assert panel.find(panel.labor_gplh)
        assert panel.find(panel.labor_lh100)
        assert panel.find(panel.labor_hours)
        assert panel.find(panel.labor_total)

        # verify elements on Forecast Data tab
        assert panel.find(panel.forecast_data_tab)
        panel.get_labor_volume()
        panel.get_chart_view()
        assert panel.find(panel.labor_forecast_chart)
