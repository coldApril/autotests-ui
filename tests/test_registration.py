import pytest
from playwright.sync_api import expect, Page
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

url = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
email = "user.name@gmail.com"
username = "username"
password = "password"

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit(url)
    registration_page.fill_registration_form(email=email, username=username, password=password)
    registration_page.click_registration_button()
    dashboard_page.check_dashboard_title()