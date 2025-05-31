from playwright.sync_api import expect, Page
import pytest
from pages.login_page import LoginPage

url = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, password", 
                         [("user.name@gmail.com", "password"), 
                          ("user.name@gmail.com", "  "), 
                          ("  ", "password")])
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit(url)
    login_page.login_form.fill_login_form(email=email, password=password)
    login_page.login_form.check_visible(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()
