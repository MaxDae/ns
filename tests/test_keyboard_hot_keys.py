import pytest

from common.common import Base
from Pages.SchedulingPage import SchedulingPage

@pytest.mark.parametrize(("username", "password"), [("autoTestUser", "testpassword123")])
class TestKeyboardHotKeys(Base):

    @pytest.mark.parametrize(("schedule_name", "employee_id"), [("Bar1", 17356253)])
    def test_copy_paste_hot_key(self, driver, base_url, username, password, schedule_name, employee_id):

        CP_hot_key = SchedulingPage(driver, base_url, username, password)
        CP_hot_key.ctrl_C(CP_hot_key.get_employee_day_for_schedule(schedule_name, employee_id, 1))
        CP_hot_key.ctrl_V(CP_hot_key.get_employee_day_for_schedule(schedule_name, employee_id, 2))
        CP_hot_key.ctrl_V(CP_hot_key.get_employee_day_for_schedule(schedule_name, employee_id, 3))
        CP_hot_key.ctrl_V(CP_hot_key.get_employee_day_for_schedule(schedule_name, employee_id, 4))
        CP_hot_key.ctrl_V(CP_hot_key.get_employee_day_for_schedule(schedule_name, employee_id, 5))
        CP_hot_key.ctrl_V(CP_hot_key.get_employee_day_for_schedule(schedule_name, employee_id, 6))
        CP_hot_key.ctrl_V(CP_hot_key.get_employee_day_for_schedule(schedule_name, employee_id, 7))
        CP_hot_key.DELETE_button(CP_hot_key.get_employee_day_for_schedule(schedule_name, employee_id, 6))

        # clean up copied shifts
        CP_hot_key.ctrl_Z(CP_hot_key.get_employee_day_for_schedule(schedule_name, employee_id, 7))
        CP_hot_key.ctrl_Z(CP_hot_key.get_employee_day_for_schedule(schedule_name, employee_id, 6))
        CP_hot_key.ctrl_Z(CP_hot_key.get_employee_day_for_schedule(schedule_name, employee_id, 5))
        CP_hot_key.ctrl_Z(CP_hot_key.get_employee_day_for_schedule(schedule_name, employee_id, 4))
        CP_hot_key.ctrl_Z(CP_hot_key.get_employee_day_for_schedule(schedule_name, employee_id, 3))
        CP_hot_key.ctrl_Z(CP_hot_key.get_employee_day_for_schedule(schedule_name, employee_id, 2))



