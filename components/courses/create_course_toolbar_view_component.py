from components.base_component import BaseComponent
from playwright.sync_api import expect

class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page):
        super().__init__(page)

        self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

    def check_visible_create_course_title(self):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text('Create course')

    def check_visible(self, is_create_course_disabled=True):
        if is_create_course_disabled:
            expect(self.create_course_button).to_be_disabled()
        else:
            expect(self.create_course_button).to_be_enabled()

    def click_create_course_button(self):
        self.create_course_button.click()