import pytest
from common.common import Base
from Pages.SchedulingPage import SchedulingPage
from modals.TemplatesModal import TemplatesModal
from modals.ModalsGeneral import ModalsElement
from selenium.common.exceptions import NoSuchElementException
from kpi_panel.KpiPanel import KpiPanelTabs

@pytest.mark.parametrize(("username", "password"), [("autoTestUser", "testpassword123")])
class TestTemplate(Base):
    def test_apply_templates(self, driver, base_url, username, password):
        template = SchedulingPage(driver, base_url, username, password)

        #apply template on the schedule
        template = template.get_templates()
        assert template.find(TemplatesModal.templates_modal)
        assert template.find(ModalsElement.disable_screen)
        assert 'Templates' in template.get_element_text(ModalsElement.modal_title)
        assert template.find(ModalsElement.modal_close_button)
        assert template.find(TemplatesModal.templates_list)
        template.find_schedule_accrodion('Bar2')
        template.expand_schedule('Bar2')
        assert template.find(TemplatesModal.edit_template_button)
        assert template.find(TemplatesModal.delete_template_button)
        template.apply_template('As_shifts')
        assert template.find(ModalsElement.loading_screen)
        assert template.find(ModalsElement.modal_bottom_message)
        assert template.find(template.post_badge)
        assert template.find(KpiPanelTabs.house_shift_badge_count)

        # delete template
        template = template.get_templates()
        template.delete_template('Shift12')

        # copy template
        template.find(TemplatesModal.copy_template_button, True)[0].click()
        # close modal
        template.find(ModalsElement.modal_close_button).click()
        # open Templates modal
        template = template.get_templates()
        assert template.find(TemplatesModal.templates_modal)
        assert template.find(ModalsElement.disable_screen)
        assert 'Templates' in template.get_element_text(ModalsElement.modal_title)
        # create new template with unassigned shift from a schedule
        template.create_new('Bar2', 'new_test_template', 'test_template_description')







