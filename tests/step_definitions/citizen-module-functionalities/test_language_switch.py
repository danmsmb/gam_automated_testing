# tests/step_definitions/test_language_switch.py
import allure
from pytest_bdd import scenarios, given, when, then, scenario
from pages.language_switch_page import LanguageSwitchPage
import pytest, random, time
from playwright.sync_api import expect, Page

@allure.title("Language switch functionality validation")
@allure.description("""
Test Steps:
1. Navigate to login page (English by default)
2. Click language switch button to change to Arabic
3. Verify login page is displayed in Arabic
4. Login as citizen user
5. Click language switch button on main page
6. Verify main page is displayed in English

This test validates the complete language switching functionality between English and Arabic.
""")
@allure.severity(allure.severity_level.NORMAL)
@scenario('../../features/citizen-features/language_switch.feature', 'Successful language switch from English to Arabic and back')
def test_language_switch():
    pass


@given("I am on the login page in English")
def navigate_to_login_page_english(page: Page):
    language_page = LanguageSwitchPage(page)
    language_page.navigate_to_login_page()
    page.wait_for_timeout(7000)  # Wait for page to load
    # Verify we start in English
    assert language_page.verify_login_page_english(), "Login page should initially be in English"


@when("I click the language switch button")
def click_language_switch_on_login(page: Page):
    LanguageSwitchPage(page).click_language_switch()
    page.wait_for_timeout(1000)  # Wait for language switch to take effect
    LanguageSwitchPage(page).click_language_switch()
    page.wait_for_timeout(3000)  # Wait for language switch to take effect


@then("the page should be displayed in Arabic")
def verify_login_page_arabic(page: Page):
    language_page = LanguageSwitchPage(page)
    expect(language_page.welcome_text_ar).to_be_visible()
    expect(language_page.login_subtitle_ar).to_be_visible()
    expect(language_page.username_label_ar).to_be_visible()
    expect(language_page.password_label_ar).to_be_visible()
    assert language_page.verify_login_page_arabic(), "Login page should be displayed in Arabic"


@when("I click the language switch button on main page")
def click_language_switch_on_main(page: Page):
    LanguageSwitchPage(page).click_language_switch()
    page.wait_for_timeout(3000)  # Wait for language switch to take effect

@given("user logs in")
def user_logs_in(page: Page, config):
    language_page = LanguageSwitchPage(page)
    language_page.navigate_to_login_page()
    page.wait_for_timeout(2000)  # Wait for page to load
    language_page.login_as_citizen(config['citizen_user'], config['citizen_password'])
    page.wait_for_timeout(5000)  # Wait for main page to load

@then("the main page should be displayed in English")
def verify_main_page_english(page: Page):
    language_page = LanguageSwitchPage(page)
    expect(language_page.upcoming_button_en).to_be_visible()
    expect(language_page.today_button_en).to_be_visible()
    expect(language_page.tomorrow_button_en).to_be_visible()
    expect(language_page.social_category_en).to_be_visible()
    assert language_page.verify_main_page_english(), "Main page should be displayed in English"