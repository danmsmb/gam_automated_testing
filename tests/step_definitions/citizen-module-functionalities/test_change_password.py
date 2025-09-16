# tests/step_definitions/test_change_password.py
import allure
from pytest_bdd import scenarios, given, when, then, parsers, scenario
from pages.change_password_page import ChangePasswordPage
import pytest, random, time
from playwright.sync_api import expect, Page

@allure.title("User changes password with valid credentials")
@allure.description("""
Test Steps:
1. Navigate to change password page
2. Enter username (dana_change_password)
3. Request OTP for password change
4. Enter valid OTP code
5. Enter new password and confirm password
6. Submit password change form
7. Verify password change success message

This test validates the complete password change flow with valid credentials.
""")
@allure.severity(allure.severity_level.CRITICAL)
@scenario('../../features/citizen-features/change_password.feature', 'Successful password change using valid data')
def test_change_password():
    pass


@given("user is on the change password page")
def user_on_change_password_page(page: Page, config):
    change_password_page = ChangePasswordPage(page)
    change_password_page.load_login_page(config)
    page.wait_for_timeout(2000)  # Wait for page to load

@when(parsers.parse("I request OTP for {username} and change password with valid data"))
def request_otp_and_change_password(page: Page, username, _pytest_bdd_example):
    password_data = _pytest_bdd_example.copy()
    
    # --- dynamic password for uniqueness ---
    ts = int(time.time())
    suffix = f"{ts}!"
    
    password_data.setdefault("username", username)
    password_data.setdefault("new_password", f"NewPassword{suffix}")
    password_data.setdefault("otp_code", "123456")  # Test OTP code
    
    # Store the new password for verification
    page.new_password_for_verification = password_data["new_password"]
    page.username_for_verification = password_data["username"]
    
    ChangePasswordPage(page).change_password_complete_flow(password_data)
    page.wait_for_timeout(2000)  # Wait for any processing

@then("the password should be changed successfully")
def verify_password_change_success(page: Page):
    change_password_page = ChangePasswordPage(page)
    
    # Verify we're back on the login page
    expect(page).to_have_url("https://gamail.dev.internal.sirenanalytics.com/gamail_web/login")
    
    # Verify login form elements are visible
    expect(change_password_page.login_username_input).to_be_visible()
    expect(change_password_page.login_password_input).to_be_visible()
    expect(change_password_page.login_button).to_be_visible()
    
    # Test login with new password to verify the password change was successful
    change_password_page.verify_login_with_new_password(
        page.username_for_verification, 
        page.new_password_for_verification
    )
    
    # Verify successful login by checking if we're redirected to the main page
    expect(page).to_have_url("https://gamail.dev.internal.sirenanalytics.com/gamail_web/citizenMain")
