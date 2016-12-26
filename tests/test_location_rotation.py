import pytest
from common.common import Base
from Pages.SchedulingPage import SchedulingPage
from modals.LocationRotationModal import LocationRotationModal
from modals.ModalsGeneral import ModalsElement


@pytest.mark.parametrize(("username", "password"), [("autoTestUser", "testpassword123")])
class TestLocationRotation(Base):
    def test_location_rotation(self, driver, base_url, username, password):
        rotation = SchedulingPage(driver, base_url, username, password)
        # open Location Rotation modal
        rotation = rotation.get_locationRotation()
        assert rotation.find(LocationRotationModal.location_rotation_modal)
        assert rotation.find(ModalsElement.disable_screen)
        # verify elements are present on the modal
        assert rotation.find(LocationRotationModal.disabled_rotate_button)
        assert rotation.find(LocationRotationModal.rotate_start_time_checkbox)
        assert rotation.find(ModalsElement.modal_cancel_button)
        assert rotation.find(ModalsElement.select_all)
        assert rotation.find(ModalsElement.select_one)
        # select all schedule and rotate location and start time
        rotation.click(ModalsElement.select_all)
        rotation.click(LocationRotationModal.rotate_start_time_checkbox)
        rotation.rotate_location()
        assert rotation.find(ModalsElement.loading_screen)
        assert rotation.find(ModalsElement.modal_bottom_message)