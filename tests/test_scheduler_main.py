import pytest
from common.common import Base
from Pages.SchedulingPage import SchedulingPage


@pytest.mark.parametrize(("username", "password"), [("autoTestUser", "testpassword123")])
class TestScheduling(Base):

    @pytest.mark.parametrize(("schedule_name"), [("House")])
    def test_main_elements(self, driver, base_url, username, password, schedule_name):
        scheduling = SchedulingPage(driver, base_url, username, password)
        scheduling.wait_until_loading_dissapear()
        assert scheduling.curr_date_compare('En_gb')
        assert scheduling.find(scheduling.filter_btn)
        assert scheduling.find(scheduling.group_button)
        assert scheduling.find(scheduling.calendar_btn)
        assert scheduling.find(scheduling.refresh_btn)
        assert scheduling.find(scheduling.show_hide_btn)
        assert scheduling.find(scheduling.refresh_btn)
        assert scheduling.find(scheduling.expand_btn)
        scheduling.click(scheduling.group_button)
        for li in scheduling.group_button:

           assert scheduling.find(li)
        assert "Schedule" in scheduling.get_element_text(scheduling.group_dropdown[1])
        assert "Location" in scheduling.get_element_text(scheduling.group_dropdown[2])
        assert "None" in scheduling.get_element_text(scheduling.group_dropdown[0])
        assert scheduling.find(scheduling.this_week_button) and "disabled" in scheduling.get_element_attribute(scheduling.this_week_button, 'class')


