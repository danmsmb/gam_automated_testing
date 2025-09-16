# tests/step_definitions/test_add_event_comment.py
import allure
from pytest_bdd import scenario, scenarios, given, when, then
from pages.add_event_comment_page import AddEventCommentPage
import pytest, random, time
from playwright.sync_api import expect, Page
@allure.title("Add comment to event")
@allure.description("""
Test Steps:
1. Navigate to events page
2. Select an event and view details
3. Enter a valid comment text
4. Select rating (1-5 stars)
5. Submit the comment
6. Verify comment is added successfully
7. Verify success message is displayed

This test validates the event commenting functionality for citizen users.
""")
@allure.severity(allure.severity_level.NORMAL)

@scenario('../../features/citizen-features/add_event_comment.feature', 'Successful event comment addition using valid data')

def test_event_comment():
    pass

@when("I navigate to event details and add a comment with valid data")
def add_event_comment_with_valid_data(page: Page, _pytest_bdd_example):
    comment_data = _pytest_bdd_example.copy()

    # --- dynamic comment for uniqueness ---
    ts = int(time.time())
    suffix = f"{ts}-{random.randint(1000,9999)}"

    comment_data.setdefault("comment_text", f"Automated test comment {suffix}")
    comment_data.setdefault("rating", 4)  # Default 4-star rating

    # Store the comment text for verification
    page.comment_text_for_verification = comment_data["comment_text"]

    AddEventCommentPage(page).add_event_comment(comment_data)
    page.wait_for_timeout(2000)  # Wait for any processing

@then("the comment should be submitted successfully")
def verify_comment_submit_success(page: Page):
    expect(page.get_by_text(page.comment_text_for_verification, exact=True),
               'Submitted comment text not found on the page').to_be_visible()