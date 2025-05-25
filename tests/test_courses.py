from playwright.sync_api import sync_playwright, expect

import pytest

url_for_registration = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
url_for_courses = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"

email = "email@mail.ru"
username = "ColdApril"
password = "password"

courses = "Courses"
there_is_not_result_text = "There is no results"
results_text = "Results from the load test pipeline will be displayed here"


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(url_for_registration)

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill(email)

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill(username)

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill(password)

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        page.goto(url_for_courses)

        # Проверка наличия заголовка
        label_courses = page.get_by_test_id("courses-list-toolbar-title-text")
        expect(label_courses).to_be_visible()
        expect(label_courses).to_have_text(courses)

        # Проверка наличия иконки
        icon_folder = page.get_by_test_id("courses-list-empty-view-icon")
        expect(icon_folder).to_be_visible()

        # Проверка наличия надписи There is no results
        there_is_no_result = page.get_by_test_id("courses-list-empty-view-title-text")
        expect(there_is_no_result).to_have_text(there_is_not_result_text)

        # Проверка наличия надписи Results from the load test pipeline will be displayed here
        result_from_the_load = page.get_by_test_id("courses-list-empty-view-description-text")
        expect(result_from_the_load).to_have_text(results_text)

        page.wait_for_timeout(5000)