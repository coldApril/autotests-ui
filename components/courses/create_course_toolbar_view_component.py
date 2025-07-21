import allure

from components.base_component import BaseComponent
from playwright.sync_api import expect

from elements.button import Button
from elements.text import Text

class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.create_course_title = Text(page, 'create-course-toolbar-title-text', "Create course")
        self.create_course_button = Button(page, 'create-course-toolbar-create-course-button', "Create course button")

    @allure.step('Check that text "Create course" is visible')
    def check_visible_create_course_title(self):
        self.create_course_title.check_visible()
        self.create_course_title.check_have_text('Create course')

    @allure.step("Check create course button is enabled or disabled")
    def check_visible(self, is_create_course_disabled=True):
        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        else:
            self.create_course_button.check_enabled()

    @allure.step("Click create course")
    def click_create_course_button(self):
        self.create_course_button.click()