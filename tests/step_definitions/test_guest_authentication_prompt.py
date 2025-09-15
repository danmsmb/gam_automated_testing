# tests/step_definitions/test_guest_authentication_prompt.py
import allure
from pytest_bdd import scenarios, given, when, then, parsers, scenario
from pages.guest_authentication_page import GuestAuthenticationPage
import pytest
from playwright.sync_api import expect, Page

@allure.title("Guest user authentication prompt validation")
@allure.description("""
Test Steps:
1. Enter as guest user (no login required)
2. Navigate to main page as guest
3. Try to access protected features (like notifications, event likes)
4. Verify authentication prompt is displayed
5. Verify login requirement message is shown

This test validates that guest users are prompted to login when accessing protected features.
""")
@allure.severity(allure.severity_level.NORMAL)
@scenario('../features/guest_authentication_prompt.feature', 'Guest user accessing protected features prompts for login')
def test_guest_authentication_prompt():
    pass


@given("user enters as guest")
def user_enters_as_guest(page: Page, config):
    guest_auth_page = GuestAuthenticationPage(page)
    guest_auth_page.load_login_page(config)
    guest_auth_page.click_enter_as_guest()
    page.wait_for_timeout(2000)  # Wait for the main page to load

@when(parsers.parse("I try to access {protected_feature}"))
def try_to_access_protected_feature(page: Page, protected_feature):
    guest_auth_page = GuestAuthenticationPage(page)
    
    if protected_feature == "notifications":
        guest_auth_page.click_notifications()
    elif protected_feature == "like_event":
        guest_auth_page.click_event_like_button()
    
    page.wait_for_timeout(1000)  # Wait for the dialog to appear


@then("I can choose to sign in or continue as guest")
def verify_authentication_options(page: Page):
    guest_auth_page = GuestAuthenticationPage(page)
    
    # Verify both buttons are visible
    expect(guest_auth_page.continue_as_guest_button).to_be_visible()
    expect(guest_auth_page.sign_in_button).to_be_visible()
    
    # Test the Sign In functionality
    guest_auth_page.click_sign_in_from_dialog()
    page.wait_for_timeout(2000)
    
    # Verify we're redirected to login page
    expect(page).to_have_url("https://gamail.dev.internal.sirenanalytics.com/gamail_web/login")
    
    # Verify login form elements are visible
    expect(guest_auth_page.username_input).to_be_visible()
    expect(guest_auth_page.password_input).to_be_visible()
    expect(guest_auth_page.login_button).to_be_visible()
