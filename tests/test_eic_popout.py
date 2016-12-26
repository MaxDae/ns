import pytest
from common.common import Base
from modals.EmployeeInformationCenter import EIC

@pytest.mark.skip
@pytest.mark.parametrize(("username", "password"), [("autoTestUser", "testpassword123")])
class TestEIC(Base):
    @pytest.mark.parametrize(("employee_id"), ['17356251'])
    def test_eic_popout(self, driver, base_url, username, password, employee_id):
        '''
        scheduling = SchedulingPage()
        scheduling.find(scheduling.sort_button).click()
        scheduling.find(scheduling.sort_dropdown[0]).click()
        '''
        EIC_modal =  EIC(driver, base_url, username, password, employee_id)



