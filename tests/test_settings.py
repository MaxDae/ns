import pytest
from common.common import Base
from Pages.SchedulingPage import SchedulingPage
from modals.SettingsModal import SettingsModal
from modals.ModalsGeneral import ModalsElement
from kpi_panel.KpiPanel import KpiPanelTabs
from selenium.common.exceptions import NoSuchElementException

@pytest.mark.parametrize(("username", "password"), [("autoTestUser", "testpassword123")])
class TestSettings(Base):
    def test_apply_settings(self, driver, base_url, username, password):
        settings = SchedulingPage(driver, base_url, username, password)
        # open settings modal

        settings = settings.get_settings()
        assert settings.find(SettingsModal.settings_modal)
        assert settings.find(ModalsElement.disable_screen)
        # verify default user settings
        assert settings.find(SettingsModal.button_save_disabled)
        assert not settings.is_element_selected(SettingsModal.preferred_name_setting)
        assert settings.is_element_selected(SettingsModal.out_time_setting)
        print settings.is_element_selected(SettingsModal.job_setting)
        assert settings.is_element_selected(SettingsModal.job_setting)
        assert settings.is_element_selected(SettingsModal.location_setting)
        assert settings.is_element_selected(SettingsModal.house_shift_manager_setting)
        assert settings.is_element_selected(SettingsModal.schedule_summary_setting)
        assert  settings.is_element_selected(SettingsModal.forecast_data_setting)
        assert settings.is_element_selected(SettingsModal.labor_budget_setting)
        assert settings.is_element_selected(SettingsModal.labor_forecast_setting)
        assert settings.is_element_selected(SettingsModal.minor_alert_setting)
        assert settings.is_element_selected(SettingsModal.availability_alert_setting)
        assert settings.is_element_selected(SettingsModal.overtime_alert_setting)
        assert not settings.is_element_present(SettingsModal.aca_setting)
        # close modal
        settings.close()
        # change setting for displaying job, location, out time
        settings.get_settings()
        settings.click(SettingsModal.job_setting)
        settings.click(SettingsModal.location_setting)
        settings.click(SettingsModal.out_time_setting)
        settings.save_settings()

        #TODO verify that job, location and out time are not dispalaing on the grid (Classic and SmartView)

        # remove all KPI panel tabs
        settings.get_settings()
        settings.click(SettingsModal.house_shift_manager_setting)
        settings.click(SettingsModal.schedule_violations_setting)
        settings.click(SettingsModal.schedule_summary_setting)
        settings.click(SettingsModal.labor_budget_setting)
        settings.click(SettingsModal.labor_forecast_setting)
        settings.click(SettingsModal.button_save)

        # verify that KPI panel tabs was removed
        assert not settings.is_element_present(KpiPanelTabs.house_shift_tab)
        assert not settings.is_element_present(KpiPanelTabs.schedule_summary_tab)
        assert not settings.is_element_present(KpiPanelTabs.labor_volume_tab)
        assert not settings.is_element_present(KpiPanelTabs.labor_budget_tab)
        assert not settings.is_element_present(KpiPanelTabs.forecast_data_tab)

        # Return to previous state
        settings.get_settings()
        settings.click(SettingsModal.house_shift_manager_setting)
        settings.click(SettingsModal.schedule_violations_setting)
        settings.click(SettingsModal.schedule_summary_setting)
        settings.click(SettingsModal.labor_budget_setting)
        settings.click(SettingsModal.labor_forecast_setting)
        settings.click(SettingsModal.job_setting)
        settings.click(SettingsModal.location_setting)
        settings.click(SettingsModal.out_time_setting)
        settings.click(SettingsModal.labor_budget_setting)
        settings.click(SettingsModal.labor_forecast_setting)
        settings.click(SettingsModal.button_save)