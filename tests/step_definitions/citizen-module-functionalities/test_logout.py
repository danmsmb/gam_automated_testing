import allure
import pytest
from playwright.sync_api import Page, expect
from pytest_bdd import when, then, scenarios, scenario

@allure.title("User logout functionality")
@allure.description("""
Test Steps:
1. User is logged in to the system
2. Click on logout icon/button
3. Confirm logout action
4. Verify user is logged out successfully
5. Verify redirection to login page

This test validates the logout functionality and proper session termination.
""")
@allure.feature("Logout")
@allure.story("Logout")
@allure.severity(allure.severity_level.CRITICAL)
@scenario('../../features/citizen-features/logout.feature', 'Logout')
def test_logout():
    pass


@when('User clicks on Logout')
def logout(page: Page):

    page.get_by_role("button", name="logout_icon").click()
    page.get_by_role("button", name="Logout").click()
    page.wait_for_timeout(2000)

@then('User should be logged out')
def verify_logout(page: Page, config):
    expect(page,
           'User is not redirected back to Applications History on success message Back button click').to_have_url(
        config['app_login_page_url'])
