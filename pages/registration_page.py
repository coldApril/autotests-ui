from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage
from playwright.sync_api import expect

class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        
        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')

    def click_registration_button(self):
        self.registration_button.click()