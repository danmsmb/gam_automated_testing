# tests/step_definitions/test_event_registration.py
import allure
from pytest_bdd import scenarios, given, when, then, scenario
from pages.event_registration_page import EventRegistrationPage
import pytest, random, time
from playwright.sync_api import expect, Page

@allure.title("Citizen registers for an event")
@allure.description("""
Test Steps:
1. Login as a citizen user
2. Navigate to main page with events list
3. Click on "View details..." for the first event
4. Click on "Register Me" button
5. Fill in registration form with valid data:
   - Name
   - Age
   - Gender selection
   - Phone number
   - Email address
   - Number of participants
   - Number of participants with disabilities
   - Number of elderly participants
6. Submit the registration form
7. Verify registration success
8. Go back to event details and verify "Register Me" button is no longer visible

This test validates the complete event registration flow for citizen users.
""")
@allure.severity(allure.severity_level.CRITICAL)
@scenario('../../features/citizen-features/event_registration.feature', 'Successful event registration with valid data')
def test_event_registration():
    pass


@pytest.fixture
def event_registration_page(page):
    return EventRegistrationPage(page)


@when("I navigate to the first event details and register with valid data")
def navigate_and_register_for_event(page: Page, _pytest_bdd_example):
    event_registration_page = EventRegistrationPage(page)
    
    # Prepare registration data
    ts = int(time.time())
    rnd = random.randint(1000, 9999)
    
    registration_data = {
        "name": f"Test User {rnd}",
        "age": "25",
        "gender": "male",
        "phone": f"0791234{rnd}",
        "email": f"test{ts}@example.com",
    }
    
    # Navigate to first event details
    event_registration_page.navigate_to_first_event_details()
    
    # Click Register Me button
    event_registration_page.click_register_me()
    
    # Fill registration form
    event_registration_page.fill_registration_form(registration_data)
    
    # Submit registration
    event_registration_page.submit_registration()



@then("the Register Me button should no longer be visible")
def verify_register_button_not_visible(page: Page):
    """Verify that the Register Me button is no longer visible after successful registration"""
    event_registration_page = EventRegistrationPage(page)
    
    event_registration_page.verify_registration_success()