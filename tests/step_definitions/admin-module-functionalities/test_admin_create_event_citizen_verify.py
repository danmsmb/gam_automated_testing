import pytest
import allure
from pytest_bdd import given, scenarios, when, then, scenario, parsers
from pages.login_page import LoginPage
from pages.admin_create_event_page import AdminCreateEventPage
from pages.citizen_event_verification_page import CitizenEventVerificationPage
import json
import time


@allure.title("Admin creates event and citizen verifies it is visible")
@allure.description("""
Test Steps:
1. Login as admin user
2. Navigate to event creation page
3. Create a new event with unique name and details
4. Verify event is created successfully
5. Logout as admin and login as citizen
6. Search for the created event
7. Verify event appears in search results with correct details

This test validates the complete flow from admin event creation to citizen verification.
""")
@allure.severity(allure.severity_level.CRITICAL)
@scenario('../../features/admin-features/admin_create_event_citizen_verify.feature', 'Admin creates event and citizen verifies it is visible')
def test_admin_create_event_citizen_verify():
    pass


@given('I am logged in as admin')
def given_logged_in_admin(page, config):
    login_page = LoginPage(page)
    
    # Navigate to login page
    page.goto(config['app_login_page_url'])
    
    # Login with admin credentials
    login_page.login("admin", config)

@when(parsers.parse('I create a new event with name "{event_name}"'))
def when_create_event(page, event_name):
    admin_create_page = AdminCreateEventPage(page)
    
    # Navigate to create event
    admin_create_page.navigate_to_create_event()
    
    # Generate unique timestamp for event names
    timestamp = str(int(time.time()))[-6:]  # Last 6 digits of timestamp
    
    # Create event data
    event_data = {
        "name_arabic": f"حدث اختبار {timestamp}",
        "name_english": f"{event_name} {timestamp}",
        "start_date": "Tuesday, September 16, 2025",
        "end_date": "Wednesday, September 17, 2025", 
        "location": "Bader",
        "category": "Technology",
        "accessibility": "Wheelchair",
        "description_arabic": "حدث تقني للاختبار من الإدارة",
        "description_english": "This is a technology event created by admin for testing purposes"
    }
    
    # Store event data for later verification
    page.add_init_script(f"window.testEventData = {json.dumps(event_data)}")
    
    # Create the event using the optimized method
    admin_create_page.create_admin_event(event_data)


@then('the event should be created successfully')
def then_event_created(page):
    admin_create_page = AdminCreateEventPage(page)
    admin_create_page.verify_event_created()


@when('I logout as admin and login as citizen')
def when_logout_admin_login_citizen(page, config):
    admin_create_page = AdminCreateEventPage(page)
    login_page = LoginPage(page)
    
    # Logout admin (navigate to login page)
    admin_create_page.logout_admin()
    
    # Login as citizen
    login_page.login("citizen", config)


@when('I search for the created event')
def when_search_for_event(page):
    verification_page = CitizenEventVerificationPage(page)
    
    # Get the event data from the page context
    event_data = page.evaluate("window.testEventData")
    event_name = event_data["name_english"]
    
    # Search for the event using the inherited method
    verification_page.search_for_event(event_name)


@then('I should find the event in search results with correct details')
def then_find_event_in_search(page):
    verification_page = CitizenEventVerificationPage(page)
    
    # Get the event data from the page context
    event_data = page.evaluate("window.testEventData")
    
    # Verify event appears in search results and details are correct
    verification_page.verify_event_found(event_data["name_english"])


@pytest.fixture(scope="session")
def config():
    with open("config.json", "r") as f:
        return json.load(f)