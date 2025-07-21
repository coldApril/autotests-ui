from playwright.sync_api import sync_playwright, expect

timeout_under_exit = 5000
url = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(url)

    login_button = page.get_by_test_id("login-page-login-button")
    expect(login_button).to_be_disabled()

    page.wait_for_timeout(timeout_under_exit)