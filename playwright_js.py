from playwright.sync_api import sync_playwright

delay_for_type = 300
timeout = 5000
url = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"
mail = "user@gmail.com"

new_text = 'New Text'
js_script = """
    (text) => { // Принимаем аргумент в JS функуии
        const title = document.getElementById('authentication-ui-course-title-text');
        title.textContent = text;
    }
    """

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Для полной загрузки веб приложения используется wait_until="networkidle"
    page.goto(url, wait_until="networkidle")

    page.evaluate(js_script, new_text)

    page.wait_for_timeout(timeout)