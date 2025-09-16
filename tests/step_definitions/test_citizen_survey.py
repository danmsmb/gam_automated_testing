# tests/step_definitions/test_citizen_survey.py
import allure
from pytest_bdd import scenarios, given, when, then, scenario
from pages.citizen_survey_page import CitizenSurveyPage
import pytest, random, time
from playwright.sync_api import expect, Page

@allure.title("Citizen submits and verifies survey submission")
@allure.description("""
Test Steps:
1. Citizen logs into the system
2. Navigate to surveys section
3. Click on the first available survey
4. Fill out the survey form with valid response
5. Submit the survey
6. Verify success message is displayed
7. Try to access the same survey again
8. Verify already submitted message appears

This test validates the complete citizen survey submission and verification flow.
""")
@allure.severity(allure.severity_level.NORMAL)
@scenario('../features/citizen_survey.feature', 'Successful survey submission and verification')
def test_citizen_survey():
    pass


@when("I navigate to the surveys section")
def navigate_to_surveys(page: Page):
    CitizenSurveyPage(page).navigate_to_surveys()


@when("I click on the first available survey")
def click_first_survey(page: Page):
    CitizenSurveyPage(page).click_first_survey()


@when("I fill out the survey with valid response")
def fill_survey_form(page: Page):
    # Generate dynamic response text for uniqueness
    ts = int(time.time())
    suffix = random.randint(1000, 9999)
    response_text = f"Automated testing feedback {ts}-{suffix}. It helps ensure quality and saves development time."
    
    CitizenSurveyPage(page).fill_survey_form(response_text)


@when("I submit the survey")
def submit_survey(page: Page):
    CitizenSurveyPage(page).submit_survey()


@then("the survey should be submitted successfully")
def verify_submission_success(page: Page):
    CitizenSurveyPage(page).confirm_submission()


@when("I try to access the same survey again")
def access_same_survey_again(page: Page):
  
    CitizenSurveyPage(page).click_first_survey()


@then("I should see the already submitted message")
def verify_already_submitted_message(page: Page):
    expect(CitizenSurveyPage(page).already_submitted_message).to_be_visible()
    CitizenSurveyPage(page).click_go_back()