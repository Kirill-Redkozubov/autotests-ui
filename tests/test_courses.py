from playwright.sync_api import Page, expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto(" https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    title_courses = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(title_courses).to_have_text("Courses")

    text_object = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(text_object).to_have_text("There is no results")
    
    icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon").locator("path")
    expect(icon).to_be_visible()
    
    text_description = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(text_description).to_have_text("Results from the load test pipeline will be displayed here")