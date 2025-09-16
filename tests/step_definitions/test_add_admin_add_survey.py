# tests/step_definitions/test_surveys.py
import allure
from pytest_bdd import scenarios, given, when, then, scenario
from pages.surveys_page import SurveysPage
import pytest, random, time
from playwright.sync_api import expect, Page
from datetime import datetime, timedelta

@allure.title("Admin creates and submits a survey")
@allure.description("""
Test Steps:
1. Login as an admin user
2. Navigate to Surveys section
3. Click "Create New Survey"
4. Fill survey form with:
   - Survey title
   - Survey description
   - Start date (today)
   - End date (future date)
   - Max responses count
5. Save the survey
6. Add a long text question
7. Publish the survey
8. Enable the survey
9. Navigate back to main app
10. Go to Surveys and find the created survey
11. Click on the survey and submit filter
12. Wait for success message
13. Click "okay" to confirm

This test validates the complete survey creation and submission flow for admin users.
""")
@allure.severity(allure.severity_level.CRITICAL)
@scenario('../features/surveys.feature', 'Complete survey creation and submission flow')
def test_survey_creation_and_submission():
    pass


@pytest.fixture
def surveys_page(page):
    return SurveysPage(page)

@given("admin is on Surveyio")
def admin_on_surveyio(page: Page, config):
    page.goto("https://gamail.dev.internal.sirenanalytics.com/surveyio_web/form/survey/list/create")

@when("I create a new survey with a long text question")
def create_new_survey(page: Page, _pytest_bdd_example):
    surveys_page = SurveysPage(page)
    
    # Prepare survey data with timestamp for uniqueness
    ts = int(time.time())
    rnd = random.randint(1000, 9999)
    
    # Calculate dates
    today = datetime.now()
    future_date = today + timedelta(days=30)
    
    survey_data = {
        "title": f"Test Survey - Automated {today.year}",
        "description": "Automated test survey for validation",
        "start_date": today.strftime("%m/%d/%Y"),
        "end_date": future_date.strftime("%m/%d/%Y"),
        "max_responses": "100"
    }
    
    question_text = "What are your thoughts on the automated testing process?"
    
    # Store survey data in page for later use
    page.survey_data = survey_data
    page.question_text = question_text
    
    # Navigate to surveys and create survey
    surveys_page.navigate_to_surveys()
    surveys_page.fill_survey_basic_info(survey_data)


@when("I save, publish, and enable the survey")
def save_publish_enable_survey(page: Page):
    surveys_page = SurveysPage(page)
    
    # Save the survey first
    surveys_page.save_survey()
    
    # Add the question
    surveys_page.add_long_text_question(page.question_text)
    
    # Publish the survey
    surveys_page.publish_survey()
    
    # Enable the survey
    surveys_page.enable_survey()


@when("I navigate to the main app and submit the survey filter")
def navigate_and_submit_survey(page: Page, config):
    surveys_page = SurveysPage(page)
    
    # Navigate to main app
    surveys_page.navigate_to_main_app(page, config)
    
    # Find and click on the created survey
    surveys_page.find_and_click_created_survey(page.survey_data["title"])
    
    # Submit the survey filter
    surveys_page.submit_survey_filter()


@then("I should see a success message and be able to confirm it")
def verify_success_message(page: Page):
    """Verify that the success message appears and can be confirmed"""
    surveys_page = SurveysPage(page)
    
    # Wait for and verify success message
    surveys_page.wait_for_success_message()
    
    # Click okay to confirm
    surveys_page.click_okay_on_success()