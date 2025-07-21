from playwright.sync_api import sync_playwright, expect

url = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
mail = "user.name@gmail.com"
username = "username"
password = "password"

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(url)

    #Проверка, что кнопка Registration задизейблена
    registration_button = page.get_by_test_id("registration-page-registration-button")
    expect(registration_button).to_be_disabled()

    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.fill(mail)

    username_input = page.get_by_test_id("registration-form-username-input").locator("input")
    username_input.fill(username)

    username_input = page.get_by_test_id("registration-form-password-input").locator("input")
    username_input.fill(password)

    #Проверка, что кнопка Registration не задизейблена
    expect(registration_button).not_to_be_disabled()
    page.wait_for_timeout(5000)

