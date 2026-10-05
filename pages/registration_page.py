from components.authentication.registration_form_component import RegistrationFormComponent
from pages.base_pages import BasePage
from playwright.sync_api import Page, expect


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.button_registration = page.get_by_test_id('registration-page-registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')

    def click_button_registration(self):
        self.button_registration.click()

    def click_login_link(self):
        self.login_link.click()
