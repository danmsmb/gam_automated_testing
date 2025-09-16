"""
Step definitions for Admin Add Place BDD tests.
Tests admin functionality for adding new places through the admin interface.
"""

import allure
import pytest, random, time
from pytest_bdd import scenarios, scenario, when, then
from playwright.sync_api import expect, Page

from pages.admin_add_place_page import AdminAddPlacePage

# Load scenarios from the feature file

@allure.title("Admin Add Place Tests")
@allure.description("""
Test Steps:
1. Login as admin user (omar)
2. Navigate to Map section from admin interface  
3. Click Add New Place button
4. Fill in place form using existing add place functionality
5. Submit the place information
6. Verify successful submission and return to side menu

This test validates the admin add place functionality reusing existing add place form logic.
""")
@allure.severity(allure.severity_level.NORMAL)
@scenario('../features/admin_add_place.feature', 'Admin successfully adds a new place')
def test_admin_add_place():
    pass


@when("I navigate to the Map section from admin interface")
@allure.step("Navigate to Map section from admin interface")
def navigate_to_map_admin(page: Page):
    """Navigate to the Map section from admin side menu."""
    admin_add_place_page = AdminAddPlacePage(page)
    admin_add_place_page.navigate_to_map()


@when("I click on Add New Place from admin map")
@allure.step("Click Add New Place from admin map")
def click_add_new_place_admin(page: Page):
    """Click the Add New Place button from admin map interface."""
    admin_add_place_page = AdminAddPlacePage(page)
    admin_add_place_page.click_add_new_place()


@when("I fill in the add place form with valid data")
@allure.step("Fill in add place form with valid data")
def fill_admin_add_place_form(page: Page, _pytest_bdd_example):
    """Fill the add place form with valid test data for admin."""
    place_data = _pytest_bdd_example.copy()

    # Generate dynamic names/descriptions for uniqueness
    ts = int(time.time())
    suffix = f"{ts}-{random.randint(1000,9999)}"

    place_data.setdefault("place_name_ar", f"مكان أدمن {suffix}")
    place_data.setdefault("place_name_en", f"Admin Place {suffix}")
    place_data.setdefault("place_details_ar", f"تفاصيل المكان من الأدمن {suffix}")
    place_data.setdefault("place_details_en", f"Admin place details {suffix}")

    admin_add_place_page = AdminAddPlacePage(page)
    # Use the existing add place form functionality
    admin_add_place_page.add_place_page.fill_place_name_ar(place_data["place_name_ar"])
    page.wait_for_timeout(1000)  # Allow time for any dynamic updates
    admin_add_place_page.add_place_page.fill_place_name_en(place_data["place_name_en"])
    page.wait_for_timeout(1000)  # Allow time for any dynamic updates
    admin_add_place_page.add_place_page.select_place_category()
    page.wait_for_timeout(1000)  # Allow time for any dynamic updates
    admin_add_place_page.add_place_page.fill_place_details_ar(place_data["place_details_ar"])
    page.wait_for_timeout(1000)  # Allow time for any dynamic updates
    admin_add_place_page.add_place_page.fill_place_details_en(place_data["place_details_en"])
    page.wait_for_timeout(1000)  # Allow time for any dynamic updates
    admin_add_place_page.add_place_page.fill_location()
    page.wait_for_timeout(1000)  # Allow time for any dynamic updates
    admin_add_place_page.save_button.click()
    page.wait_for_timeout(2000)  # Wait for any processing


@then('the page URL should be "https://gamail.dev.internal.sirenanalytics.com/gamail_web/sideMenu"')
@allure.step("Verify page URL is side menu")
def verify_admin_page_url(page: Page):
    """Verify that we're back at the admin side menu page."""
    admin_add_place_page = AdminAddPlacePage(page)
    current_url = admin_add_place_page.get_current_page_url()
    expected_url = "https://gamail.dev.internal.sirenanalytics.com/gamail_web/sideMenu"
    assert expected_url in current_url, f"Expected URL to contain {expected_url}, but got {current_url}"