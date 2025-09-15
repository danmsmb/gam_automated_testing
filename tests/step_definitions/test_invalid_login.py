# tests/step_definitions/test_invalid_login.py
import allure
from pytest_bdd import scenarios, given, when, then, parsers, scenario
from pages.login_page import LoginPage
import pytest
from playwright.sync_api import expect, Page

@allure.title("Invalid login credentials validation")
@allure.description("""
Test Steps:
1. Navigate to login page
2. Enter valid username (tia)
3. Enter invalid password
4. Click login button
5. Verify error message is displayed
6. Verify user remains on login page

This test validates the login functionality with invalid credentials and proper error handling.
""")
@allure.severity(allure.severity_level.NORMAL)
@scenario('../features/invalid_login.feature', 'Login with invalid credentials shows error message')
def test_invalid_login():
    pass


@given("user is on the login page")
def user_on_login_page(page: Page, config):
    login_page = LoginPage(page)
    login_page.load(config)
    page.wait_for_timeout(2000)  # Wait for page to load

@when(parsers.parse("I attempt to login with {username} and {invalid_password}"))
def attempt_login_with_invalid_credentials(page: Page, username, invalid_password):
    login_page = LoginPage(page)
    
    # Store the credentials for verification
    page.test_username = username
    page.test_password = invalid_password
    
    login_page.attempt_invalid_login(username, invalid_password)

@then("I should see an error message")
def verify_error_message_appears(page: Page):
    login_page = LoginPage(page)
    
    # Verify the error message is visible
    expect(login_page.error_message).to_be_visible(timeout=10000)
    
    # Verify the error message contains expected text
    error_text = login_page.get_error_message_text()
    assert "Invalid username or password" in error_text, f"Expected error message not found. Actual: {error_text}"

@then("I should remain on the login page")
def verify_remain_on_login_page(page: Page):
    login_page = LoginPage(page)
    
    # Verify we're still on the login page
    expect(page).to_have_url("https://gamail.dev.internal.sirenanalytics.com/gamail_web/login")
    
    
    # Verify login button is still visible
    expect(login_page.login_button).to_be_visible()
    
    # Verify we can see the login prompt elements
    login_elements_visible = (
        login_page.welcome_text.is_visible() or 
        login_page.login_prompt_text.is_visible()
    )
    assert login_elements_visible, "Login page elements not visible"
