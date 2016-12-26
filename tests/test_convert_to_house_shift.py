import pytest
from common.common import Base
from Pages.SchedulingPage import SchedulingPage
from modals.ConvertToHouseShiftModal import ConvertToHouseShift
from modals.ModalsGeneral import ModalsElement
from kpi_panel.KpiPanel import KpiPanelTabs


@pytest.mark.parametrize(("username", "password"), [("", "")])
class TestConvertHouseShift(Base):
    def test_converting(self, driver, base_url, username, password):
        converting = SchedulingPage(driver, base_url, username, password)
        # open Convert To House Shift modal
        converting = converting.get_convertTo_house()
        assert converting.find(ModalsElement.disable_screen)
        assert converting.find(ConvertToHouseShift.convert_to_house_shift_modal)
        # verify elements are present on the modal
        assert converting.find(ConvertToHouseShift.button_ok_disabled)
        assert converting.find(ModalsElement.modal_cancel_button)
        assert converting.find(ModalsElement.select_all)
        assert converting.find(ModalsElement.select_one)
        # select all schedule and convert shift into house shifts
        converting.click(ModalsElement.select_all)
        converting.convert_action()
        assert converting.find(ModalsElement.loading_screen)
        assert converting.find(ModalsElement.modal_bottom_message)
        assert converting.find(KpiPanelTabs.house_shift_badge_count)