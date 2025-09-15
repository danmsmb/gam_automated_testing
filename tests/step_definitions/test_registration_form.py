# tests/step_definitions/registration_steps.py
import allure
from pytest_bdd import scenarios, given, when, then, scenario
from pages.registration_page import RegistrationPage
import pytest, random, time
from playwright.sync_api import expect, Page

@allure.title("User registration with valid data")
@allure.description("""
Test Steps:
1. Navigate to registration page
2. Fill in personal information (username, email, phone)
3. Set password and confirm password
4. Select gender and age
5. Choose location
6. Submit registration form
7. Verify registration success message
8. Verify user is redirected to login page

This test validates the complete user registration flow with valid data.
""")
@allure.severity(allure.severity_level.CRITICAL)
@scenario('../features/registration.feature', 'Successful user registration with valid data')
def test_registration():
    pass
@pytest.fixture
def registration_page(page):
    return RegistrationPage(page)

@given('User is on the registration page')
def user_on_registration_page(page: Page, config):
    RegistrationPage(page).load(config)

@when("I fill in the registration form with the following details:")
def fill_registration_form(page, _pytest_bdd_example):
    user_data = _pytest_bdd_example.copy()

    # Dynamic data
    ts = int(time.time()); rnd = random.randint(1000, 9999)
    if user_data.get("username") == "auto_username":
        user_data["username"] = f"user_{ts}_{rnd}"
    if user_data.get("phone_number") == "auto_phone":
        user_data["phone_number"] = f"96279{random.randint(1000000, 9999999)}"
    if user_data.get("national_personal_number") == "auto_npn":
        user_data["national_personal_number"] = f"{ts}{random.randint(100,999)}"
    if user_data.get("national_id_number") == "auto_idn":
        user_data["national_id_number"] = f"{ts}{random.randint(200,999)}"

    RegistrationPage(page).registration(user_data)

@then('the registration should be completed successfully')
def verify_registration_success(registration_page, config):
    expect(registration_page.page).to_have_url(config['app_home_page_url'])
