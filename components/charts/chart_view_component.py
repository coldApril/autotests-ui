from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        self.identifiers = identifier

        self.title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

        self.students_chart_title = page.get_by_test_id("students-widget-title-text") 
        self.activities_chart_title = page.get_by_test_id("activities-widget-title-text")
        self.courses_chart_title = page.get_by_test_id("courses-widget-title-text")
        self.scores_chart_title = page.get_by_test_id("scores-widget-title-text")

    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.chart).to_be_visible()

        if self.identifiers == "scores":
            expect(self.scores_chart_title).to_have_text('Scores')
        elif self.identifiers == "courses":
            expect(self.courses_chart_title).to_have_text('Courses')
        elif self.identifiers == "students":
            expect(self.students_chart_title).to_have_text('Students')
        elif self.identifiers == "activites":
            expect(self.activities_chart_title).to_have_text('Activities')
        
        
