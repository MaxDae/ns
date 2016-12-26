__author__ = 'mvasin'

import pytest
from common.common import Base
from Pages.SchedulingPage import SchedulingPage
from modals.AutoScheduleModal import AutoScheduleModal


@pytest.mark.parametrize(("username", "password", "schedule_id"), [("autoTestUser", "testpassword123", "1024432433")])
@pytest.mark.parametrize("jobLocationMap",)
class TestSample(Base)

    @classmethod
    def setup_class(cls, jobLocationMap, username, password):
        jl_map = jobLocationMap(username, password)



     def test_austoschedule(self, driver, base_url, username, password, schedule_id, jl_map):
        print