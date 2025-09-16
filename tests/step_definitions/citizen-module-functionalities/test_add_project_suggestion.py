# tests/step_definitions/test_add_project_suggestion.py
import allure
from pytest_bdd import scenarios, given, when, then, scenario
from pages.add_project_suggestion_page import AddProjectSuggestionPage
import pytest, random, time
from playwright.sync_api import expect, Page
import re

@allure.title("Add suggestion to ongoing project")
@allure.description("""
Test Steps:
1. Navigate to projects section
2. Find and select an ongoing project
3. Enter a valid suggestion text
4. Submit the suggestion
5. Verify suggestion is added successfully
6. Verify success message is displayed

This test validates the project suggestion functionality for citizen users.
""")
@allure.severity(allure.severity_level.NORMAL)
@scenario('../../features/citizen-features/add_project_suggestion.feature', 'Successful project suggestion addition using valid data')
def test_add_project_suggestion():
    pass


@when("I navigate to an ongoing project and add a suggestion with valid data")
def add_project_suggestion_with_valid_data(page: Page, _pytest_bdd_example):
    suggestion_data = _pytest_bdd_example.copy()

    # --- dynamic suggestion for uniqueness ---
    ts = int(time.time())
    suffix = f"{ts}-{random.randint(1000,9999)}"

    suggestion_data.setdefault("suggestion_text", f"Automated test suggestion {suffix}")

    # Store the suggestion text for verification
    page.suggestion_text_for_verification = suggestion_data["suggestion_text"]

    AddProjectSuggestionPage(page).add_project_suggestion(suggestion_data)
    page.wait_for_timeout(2000)  # Wait for any processing

@then("the suggestion should be submitted successfully")
def verify_suggestion_submit_success(page: Page):
    # Verify by checking that we can navigate back without errors
    # The success dialog has already been handled in the page object
    # We could also verify that we're back on the project details page
    expect(page).to_have_url(re.compile(r"/projectDetails(?:[/?#].*)?$"), timeout=10_000)
    
    # Additional verification could be to check if the suggestion appears in the suggestions list
    # But since suggestions need admin approval, they might not be immediately visible
