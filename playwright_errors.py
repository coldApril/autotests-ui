from playwright.sync_api import sync_playwright, expect

url = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
mail = "user@gmail.com"

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(url)

    # unknown = page.locator("unknown")
    # expect(unknown).to_be_visible()

    # login_button = page.get_by_test_id("login-page-login-button")
    # login_button.fill("unknown")