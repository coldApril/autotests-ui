from playwright.sync_api import Page, expect
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage

import pytest

url_for_registration = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
url_for_courses = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
url_for_create_courses = " https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create"

email = "email@mail.ru"
username = "ColdApril"
password = "password"

courses = "Courses"
there_is_not_result_text = "There is no results"
results_text = "Results from the load test pipeline will be displayed here"


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page, ):
    chromium_page_with_state.goto(url_for_courses)

    # Проверка наличия заголовка
    label_courses = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(label_courses).to_be_visible()
    expect(label_courses).to_have_text(courses)

    # Проверка наличия иконки
    icon_folder = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(icon_folder).to_be_visible()

    # Проверка наличия надписи There is no results
    there_is_no_result = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(there_is_no_result).to_have_text(there_is_not_result_text)

    # Проверка наличия надписи Results from the load test pipeline will be displayed here
    result_from_the_load = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(result_from_the_load).to_have_text(results_text)


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_course_page.visit(url_for_create_courses)
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(
        title="",
        description="",
        estimated_time="",
        max_score="0",
        min_score="0"
    )
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image("./testdata/files/image.png")
    create_course_page.check_visible_image_upload_view()
    create_course_page.fill_create_course_form(
        title = "Playwright",
        estimated_time = "2 weeks",
        description = "Playwright",
        max_score = "100",
        min_score = "10"
    )
    create_course_page.click_create_course_button()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index = "0",
        title = "Playwright",
        estimated_time = "2 weeks",
        max_score = "100",
        min_score = "10"
    )