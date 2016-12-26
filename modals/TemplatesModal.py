
from selenium.webdriver.common.by import By
from modals.ModalsGeneral import ModalsElement
from selenium.common.exceptions import NoSuchElementException, ElementNotSelectableException

class TemplatesModal (ModalsElement):
    templates_menu_item = (By.CSS_SELECTOR, "div.dropdown-container li.item[data-tool=templates]")
    templates_modal = (By.CSS_SELECTOR, "div.schedule-templates-modal")
    templates_list = (By.CSS_SELECTOR, "li.schedule-templates")
    schedule_template_name = (By.CSS_SELECTOR, "div.templates div.name")
    schedule_template_description = (By.CSS_SELECTOR, "div.templates div.description")
    edit_template_button = (By.CSS_SELECTOR, "div.schedule-templates-modal a.edit.button")
    copy_template_button = (By.CSS_SELECTOR, "div.schedule-templates-modal button.duplicate i.ico.content_copy")
    delete_template_button = (By.CSS_SELECTOR, "div.schedule-template button.delete.button.icon i.ico.delete")
    apply_template_button = (By.CSS_SELECTOR, "div.schedule-templates-modal button.apply.button.link")
    create_new_template_link = (By.XPATH, "//span[@class='ui-dialog-title']/ancestor::div/ancestor::div/descendant::button[@class='button link']")
    create_new_template_name = (By.CSS_SELECTOR, "div.new-template.collapsible-content input[name=newName]")
    create_new_template_description = (By.CSS_SELECTOR, "div.new-template.collapsible-content input[name=newDescription]")
    create_new_template_button = (By.CSS_SELECTOR, "div.new-template.collapsible-content button.create.button.link")
    create_assigned_template_button = (By.CSS_SELECTOR, "div.new-template.collapsible-content input[type=radio][value=assigned]")
    create_unassigned_template_button = (By.CSS_SELECTOR, "div.new-template.collapsible-content input[type=radio][checked][value=unassigned]")
    create_from_schedule = (By.CSS_SELECTOR, "//button[@class='button link']")
    close_templates_modal_button = (By.CSS_SELECTOR, "div.schedule-templates-modal button.primary.close")
    # delete_confirmation_modal = (By.XPATH, "//span[text()='Delete Template']/ancestor::div[@role='dialog']")
    delete_confirmation_modal = (By.CSS_SELECTOR, "div.confirm-delete-template")
    delete_confirmation_modal_button = (By.XPATH, "//span[text()='Delete Template']/ancestor::div[@role='dialog']/descendant::button[@class='button primary']")
    # apply_template_confirmation_modal = (By.XPATH, "//span[text()='Bar1 schedule']/ancestor::div[@role='dialog']")
    apply_template_confirmation_modal = (By.CSS_SELECTOR, "div.confirm-apply-template")
    apply_template_confirmation_button =(By.XPATH,"//span[text()='Bar1 schedule']/ancestor::div[@role='dialog']/descendant::button[@class='button primary']")
    apply_template_btn = (By.XPATH, "//button[@class='apply button link' and contains(., div[contains(., '{0}')])]")
    delete_template_btn = (By.XPATH, "//button[@class='delete button icon' and contains(., div[contains(., '{0}')])]")
    copy_template_btn = (By.XPATH, "//button[@class='duplicate button icon' and contains(., div[contains(., '{0}')])]")
    schedule_accordion = (By.XPATH, "//li[@class='schedule-templates']/div[contains(.,'{0}')]")
    confirm_btn = (By.XPATH, "//button[@class='button primary']")

    def __init__(self, driver):
        self.driver = driver

    def find_schedule_accrodion(self, schedule_name):
        schedule_accordion = list(self.schedule_accordion)
        schedule_accordion[1].format(schedule_name)
        return self.find(tuple(schedule_accordion))

    def apply_template(self, template_name):
        apply_btn = list(self.apply_template_btn)
        apply_btn[1].format(template_name)


        self.click(tuple(apply_btn))
        try:
            self.find(self.confirm_btn)
            self.confirm()
        except NoSuchElementException:
           pass

    def copy_template(self, template_name):
        copy_btn = list(self.copy_template_button)
        copy_btn[1].format(template_name)
        return self.click(tuple(copy_btn))

    def delete_template(self, template_name):
        delete_btn = list(self.delete_template_btn)
        delete_btn[1].format(template_name)
        return self.click(tuple(delete_btn))

    def expand_schedule(self, schedule_name):
        schedule_accordion = list(self.schedule_accordion)
        schedule_accordion[1].format(schedule_name)
        return self.click(tuple(schedule_accordion))

    def create_new(self, schedule_name, name, description, unasigned = True):
        self.expand_schedule(schedule_name)
        self.click(self.create_from_schedule)
        if not unasigned:
            self.click(self.create_assigned_template_button)
        self.send_text(self.create_new_template_name, name)
        self.send_text(self.create_new_template_description, name)
        self.click(self.create_new_template_button)

    def confirm(self):
        self.click(self.confirm_btn)
