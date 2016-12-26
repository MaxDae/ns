import pytest

from common.common import Base
from Pages.SchedulingPage import SchedulingPage



@pytest.mark.parametrize(("username", "password"), [("", "")])
class TestAddShiftModal(Base):

    @pytest.mark.parametrize(("schedule_name", "employee_id"), [("Bar1", '\'17356253\'')])
    def test_add_shift(self, driver, base_url, username, password, schedule_name, employee_id):

        add_shift_modal = SchedulingPage(driver, base_url, username, password).add_shift(3, employee_id)
        #assert "Back" not in scheduling.get_filter_schedules_names()
        #assert scheduling.filter_btn
        #add_shift_modal = scheduling.add_shift(3,employee_id )
        #add_shift_modal = scheduling.get_add_shift_modal(3,'\'16890087\'' )
        #assert NoSuchElementException in add_shift_modal.find(add_shift_modal.no_such_element)
        assert 'Cara Valdez' in add_shift_modal.get_full_name()
        #assert add_shift_modal.find(add_shift_modal.shift_modal_constraints)
        assert add_shift_modal.find(add_shift_modal.shift_modal_cancel)
        assert add_shift_modal.find(add_shift_modal.shift_modal_start_time)
        assert add_shift_modal.find(add_shift_modal.shift_modal_end_time)
        assert add_shift_modal.find(add_shift_modal.shift_modal_job)
        assert add_shift_modal.find(add_shift_modal.shift_modal_location)
        assert add_shift_modal.find(add_shift_modal.shift_modal_delete_icon)


        add_shift_modal.fill('08:00', '16:00', 'Bartender1', 'Bar1')
        assert add_shift_modal.get_total_per_shift() == 8.00
        assert "Bartender1" in add_shift_modal.get_element_text(add_shift_modal.shift_modal_timeline_content)
        add_shift_modal.save()







