from playwright.sync_api import sync_playwright

url = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
mail = "user@gmail.com"
delay_for_type = 300

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(url)

    email_input = page.get_by_test_id("login-form-email-input").locator("input")
    email_input.focus()

    for char in mail:
        page.keyboard.type(char, delay=delay_for_type)

    page.keyboard.press("ControlOrMeta+A")

    page.wait_for_timeout(5000)