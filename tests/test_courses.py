from playwright.sync_api import Page, expect
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage

import pytest

url_for_registration = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
url_for_courses = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
url_for_create_courses = " https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create"

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit(url_for_courses)

    courses_list_page.sidebar.check_visible()
    courses_list_page.navbar.check_visible("username")

    courses_list_page.check_visible_empty_view()
    courses_list_page.toolbar_view.check_visible()

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_course_page.visit(url_for_create_courses)
    create_course_page.create_course_toolbar_view.check_visible_create_course_title()
    create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=True)
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
    create_course_page.create_course_form.check_visible_create_course_form(
        title="",
        description="",
        estimated_time="",
        max_score="0",
        min_score="0"
    )
    create_course_page.create_course_exercises_toolbar_view.check_visible_exercises_title()
    create_course_page.create_course_exercises_toolbar_view.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
    create_course_page.create_course_form.fill_create_course_form(
        title = "Playwright",
        estimated_time = "2 weeks",
        description = "Playwright",
        max_score = "100",
        min_score = "10"
    )
    create_course_page.create_course_form.check_visible_create_course_form(
        title = "Playwright",
        estimated_time = "2 weeks",
        description = "Playwright",
        max_score = "100",
        min_score = "10"
    )
    create_course_page.create_course_toolbar_view.check_visible(is_create_course_disabled=False)
    create_course_page.create_course_toolbar_view.click_create_course_button()
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible(
    index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
)