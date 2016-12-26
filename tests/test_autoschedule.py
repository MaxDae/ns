import pytest
from common.common import Base
from Pages.SchedulingPage import SchedulingPage
from modals.AutoScheduleModal import AutoScheduleModal



@pytest.mark.parametrize(("username", "password", "schedule_id"), [("", "", "")])
#@pytest.mark.usefixtures('resource')
class TestAutoschedule(Base):





    def test_austoschedule(self, driver, base_url, username, password, schedule_id):
        autoschedule = SchedulingPage(driver, base_url, username, password)

        autoschedule = autoschedule.get_autoscheduler()
        assert autoschedule.find(AutoScheduleModal.auto_schedule_modal)
        assert autoschedule.find(AutoScheduleModal.disable_screen)
        # verify elements is present on Auto-Schedule modal
        assert 'Auto-Schedule' in autoschedule.get_element_text(AutoScheduleModal.modal_title)
        assert autoschedule.find(AutoScheduleModal.modal_close_button)
        assert autoschedule.find(AutoScheduleModal.generate_schedule_button)
        assert autoschedule.find(AutoScheduleModal.schedule_name_checkbox)
        assert autoschedule.find(AutoScheduleModal.select_auto_schedule_settings)
        assert autoschedule.find(AutoScheduleModal.auto_schedule_house_shift)
        assert autoschedule.is_element_selected(autoschedule.auto_schedule_house_shift)

        assert autoschedule.find(AutoScheduleModal.auto_schedule_assigned_shifts)
        assert autoschedule.find(AutoScheduleModal.honor_request_off_option)
        assert autoschedule.is_element_selected(autoschedule.honor_request_off_option)
        assert autoschedule.find(AutoScheduleModal.allow_employee_multiple_shifts)
        assert autoschedule.find(AutoScheduleModal.schedule_shifts_on_unavailable_day)
        assert autoschedule.find(AutoScheduleModal.use_location_limits_per_work_week)
        assert autoschedule.find(AutoScheduleModal.no_skill_level_rule)
        assert autoschedule.find(AutoScheduleModal.use_skill_level_rule)
        #assert autoschedule.find(AutoScheduleModal.use_location_skill_levels)

        assert autoschedule.find(AutoScheduleModal.max_allowable_hours_input_field)
        assert autoschedule.get_element_attribute(autoschedule.max_allowable_hours_input_field, "value") == "40.0"
        assert autoschedule.get_element_attribute(autoschedule.max_allowable_days_input_field, "value") == "5"
        assert autoschedule.get_element_attribute(AutoScheduleModal.auto_schedule_house_shift, 'value') == 'true'
        #select schedule and autoschedule shift
        autoschedule.select_schedule(schedule_id)
        autoschedule.generate()
        #assert autoschedule.find(AutoScheduleModal.loading_screen)
        #assert 'Schedule(s) generated' in autoschedule.get_element_text(AutoScheduleModal.modal_bottom_message)



