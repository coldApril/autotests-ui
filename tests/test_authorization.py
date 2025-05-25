from playwright.sync_api import sync_playwright, expect

url = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
email = 'user.name@gmail.com'
password = 'password'
warning_label = 'Wrong email or password'


def test_wrong_email_or_password_authorization():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(url)

        email_input = page.get_by_test_id("login-form-email-input").locator("input")
        email_input.fill(email)

        password_input = page.get_by_test_id("login-form-password-input").locator("input")
        password_input.fill(password)

        login_button = page.get_by_test_id("login-page-login-button")
        login_button.click()

        wrong_email_or_password = page.get_by_test_id("login-page-wrong-email-or-password-alert")
        expect(wrong_email_or_password).to_be_visible()
        expect(wrong_email_or_password).to_have_text(warning_label)
