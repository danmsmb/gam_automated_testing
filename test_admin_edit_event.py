import pytest
from pytest_bdd import given, scenarios, when, then, parsers
from pages.login_page import LoginPage
from pages.admin_create_event_page import AdminCreateEventPage
import json
import time

#this test is for later, when edit suggest form locators are fixed.

scenarios('../features/admin_edit_event.feature')


@given('I am logged in as admin')
def given_logged_in_admin(page, config):
    login_page = LoginPage(page)
    
    # Navigate to login page
    page.goto(config['app_login_page_url'])
    
    # Login with admin credentials
    login_page.login("admin", config)


@when('I navigate to manage events')
def when_navigate_to_manage_events(page):
    admin_page = AdminCreateEventPage(page)
    admin_page.navigate_to_manage_events()


@when(parsers.parse('I edit an existing event name to "{new_name}"'))
def when_edit_event_name(page, new_name):
    admin_page = AdminCreateEventPage(page)
    
    # Generate unique timestamp for event names
    timestamp = str(int(time.time()))[-6:]  # Last 6 digits of timestamp
    unique_event_name = f"{new_name} {timestamp}"
    
    # Store the unique name for later verification
    page.add_init_script(f"window.testUpdatedEventName = '{unique_event_name}'")
    
    admin_page.edit_first_event_name(unique_event_name)


@then('the event should be updated successfully')
def then_event_updated_successfully(page):
    admin_page = AdminCreateEventPage(page)
    admin_page.verify_event_updated_successfully()


@when('I navigate to dashboard')
def when_navigate_to_dashboard(page):
    admin_page = AdminCreateEventPage(page)
    admin_page.navigate_to_dashboard()


@when(parsers.parse('I search for "{search_term}"'))
def when_search_for_event(page, search_term):
    admin_page = AdminCreateEventPage(page)
    
    # Get the actual updated event name from the page context
    updated_event_name = page.evaluate("window.testUpdatedEventName")
    
    admin_page.search_for_event(updated_event_name)


@then('I should find the updated event in search results')
def then_find_updated_event(page):
    admin_page = AdminCreateEventPage(page)
    
    # Get the actual updated event name from the page context
    updated_event_name = page.evaluate("window.testUpdatedEventName")
    
    admin_page.verify_event_found_in_search(updated_event_name)


@pytest.fixture(scope="session")
def config():
    with open("config.json", "r") as f:
        return json.load(f)