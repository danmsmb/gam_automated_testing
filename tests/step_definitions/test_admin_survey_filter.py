# tests/step_definitions/test_admin_survey_filter.py
import allure
from pytest_bdd import scenarios, given, when, then, scenario
from pages.admin_survey_filter_page import AdminSurveyFilterPage
import pytest, random, time
from playwright.sync_api import expect, Page

@allure.title("Admin creates survey filter template")
@allure.description("""
Test Steps:
1. Admin logs into the system
2. Navigate to survey filter templates section
3. Click create new survey template button
4. Fill out the template form with valid data:
   - Target group name
   - Location (Bader)
   - Gender (All)
   - Age sliders (keep as is)
5. Submit the survey filter template
6. Verify okay button is visible (indicating success)

This test validates the complete admin survey filter template creation flow.
""")
@allure.severity(allure.severity_level.NORMAL)
@scenario('../features/admin_survey_filter.feature', 'Successful survey filter template creation')
def test_admin_survey_filter():
    pass


@when("I navigate to survey filter templates section")
def navigate_to_survey_filter_templates(page: Page):
    AdminSurveyFilterPage(page).navigate_to_survey_filter_templates()


@when("I click create new survey template")
def click_create_new_template(page: Page):
    AdminSurveyFilterPage(page).click_create_new_template()


@when("I fill the survey filter template with valid data")
def fill_survey_filter_template(page: Page):
    # Generate dynamic template name for uniqueness
    ts = int(time.time())
    suffix = random.randint(1000, 9999)
    template_name = f"Test Survey Filter Template - Automated {ts}-{suffix}"
    
    admin_page = AdminSurveyFilterPage(page)
    admin_page.fill_target_group_name(template_name)
    admin_page.select_location()
    admin_page.select_gender_all()



@when("I submit the survey filter template")
def submit_survey_filter_template(page: Page):
    AdminSurveyFilterPage(page).submit_template()


@then("the okay button should be visible")
def verify_okay_button_visible(page: Page):
    admin_page = AdminSurveyFilterPage(page)
    expect(admin_page.okay_button).to_be_visible()
    # Close the success dialog
    admin_page.click_okay_button()