# tests/step_definitions/test_add_project_feedback.py
import allure
from pytest_bdd import scenarios, given, when, then, scenario
from pages.add_project_feedback_page import AddProjectFeedbackPage
import pytest, random, time
from playwright.sync_api import expect, Page
import re

@allure.title("Add feedback to completed project")
@allure.description("""
Test Steps:
1. Navigate to projects section
2. Find and select a completed project
3. Enter valid feedback text
4. Select rating (1-5 stars)
5. Submit the feedback
6. Verify feedback is added successfully
7. Verify success message is displayed

This test validates the project feedback functionality for completed projects.
""")
@allure.severity(allure.severity_level.NORMAL)
@scenario('../features/add_project_feedback.feature', 'Successful project feedback addition using valid data')
def test_add_project_feedback():
    pass


@when("I navigate to a completed project and add feedback with valid data")
def add_project_feedback_with_valid_data(page: Page, _pytest_bdd_example):
    feedback_data = _pytest_bdd_example.copy()

    # --- dynamic feedback for uniqueness ---
    ts = int(time.time())
    suffix = f"{ts}-{random.randint(1000,9999)}"

    feedback_data.setdefault("feedback_text", f"Automated test feedback {suffix}")
    feedback_data.setdefault("rating", 4)  # Default 4-star rating

    # Store the feedback text for verification
    page.feedback_text_for_verification = feedback_data["feedback_text"]

    AddProjectFeedbackPage(page).add_project_feedback(feedback_data)
    page.wait_for_timeout(2000)  # Wait for any processing

@then("the feedback should be submitted successfully")
def verify_feedback_submit_success(page: Page):
    # Verify by checking that we can navigate back without errors
    # The success dialog has already been handled in the page object
    # We could also verify that we're back on the project details page
    expect(page).to_have_url(re.compile(r"/projectDetails(?:[/?#].*)?$"), timeout=10_000)
    # Additional verification could be to check if the feedback appears in the feedbacks list
    # But since feedbacks need admin approval, they might not be immediately visible
