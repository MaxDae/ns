__author__ = 'mvasin'
import pytest
from common.common import Base
from Pages.SchedulingPage import SchedulingPage



@pytest.mark.parametrize(("username", "password"), [("autoTestUser", "testpassword123")])
class TestScheduling(Base):



    def test_filters_population(self, driver, base_url, username, password):
        scheduling = SchedulingPage(driver, base_url, username, password)
        fm = scheduling.get_filters()
        fm.set_job("Host")
        fm.set_schedule("Cook")
        assert "hidden" in fm.get_element_attribute(fm.locations_sticky_filters_delimiter, "class")
        assert "hidden" in fm.get_element_attribute(fm.schedules_sticky_filters_delimiter, "class")
        assert "hidden" in fm.get_element_attribute(fm.jobs_sticky_filters_delimiter, "class")

        assert fm.is_element_selected(fm.get_schedule("Cook"))
        assert fm.is_element_selected(fm.get_job("Host"))
        assert fm.get_schedules_count() == 1
        assert fm.get_jobs_count() == 1
        # Unselect selected schedule
        fm.set_job("Host")
        fm.set_schedule("Cook")
        assert fm.get_schedules_count() == 0
        assert fm.get_jobs_count() == 0
        assert not fm.is_element_selected(fm.get_schedule("Cook"))
        assert not fm.is_element_selected(fm.get_job("Host"))
        # Select again
        fm.set_job("Host")
        fm.set_schedule("Cook")
        # Unselect by Clear All
        fm.clear_all()
        assert fm.get_schedules_count() == 0
        assert fm.get_jobs_count() == 0
        assert not fm.is_element_selected(fm.get_schedule("Cook"))
        assert not fm.is_element_selected(fm.get_job("Host"))
        # Verify that sticky delimiter displays
        fm.set_location("Appet")
        fm.set_location("Bar1")
        fm.set_location("bar2")
        fm.set_location("Clean1")
        fm.set_location("Clean2")
        assert fm.get_locations_count() == 5
        fm.click(fm.filter_locations_nextPage)
        fm.click(fm.filter_locations_previousPage)
        assert not "hidden" in fm.get_element_attribute(fm.locations_sticky_filters_delimiter, "class")
        #Verify that "Show more and Show less displays behind the sticky filters delimiter
        fm.set_location("Clean3")
        fm.click(fm.filter_locations_nextPage)
        fm.click(fm.filter_locations_previousPage)
        assert "+ 1 more" in fm.get_element_text(fm.locations_more_sticky_filters)
        fm.click(fm.locations_more_sticky_filters)
        assert not "hidden" in fm.get_element_attribute(fm.locations_less_sticky_filters, "class")
        assert "show less" in fm.get_element_text(fm.locations_less_sticky_filters)
        fm.clear_all()
        assert fm.get_locations_count() == 0
        #Verify that checkbox is not selected after clear All pressed
        assert not fm.is_element_selected(fm.get_location("Appet"))
        assert not fm.is_element_selected(fm.get_location("Bar1"))
        assert not fm.is_element_selected(fm.get_location("bar2"))
        assert not fm.is_element_selected(fm.get_location("Clean1"))
        assert not fm.is_element_selected(fm.get_location("Clean2"))
        assert not fm.is_element_selected(fm.get_location("Clean3"))

        # Verify if Job - Location populating works well
        fm.set_job("Host")
        fm.set_schedule("Cook")

        assert "HLoc1" in fm.get_filter_names("Location")
        assert "Hloc2" in fm.get_filter_names("Location")
        assert "Unassigned" in fm.get_filter_names("Location")
        assert not "Clok2" in fm.get_filter_names("Location")



    @pytest.mark.parametrize(("schedule_name, employee_id"), [("Cook", 17356255)])
    def test_employee_by_job_filter(self, driver, base_url, username, password, schedule_name, employee_id):
        scheduling = SchedulingPage(driver, base_url, username, password)
        fm = scheduling.get_filters()
        fm.set_job("Host")
        fm.set_schedule("Cook")
        fm.apply()

        # Verify if after filter applies and employee for selected filter shows on a grid
        scheduling.is_element_present(scheduling.get_employee_day_for_schedule(schedule_name,employee_id, 1))
        fm.open()
        fm.clear_all()
        fm.apply()
        assert scheduling.is_element_present(scheduling.get_employee_day_for_schedule(schedule_name,employee_id, 1))


