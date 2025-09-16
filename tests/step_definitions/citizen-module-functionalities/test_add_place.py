# tests/step_definitions/add_place_steps.py
import allure
from pytest_bdd import scenarios, given, when, then, scenario
from pages.add_place_page import AddPlacePage
import pytest, random, time
from playwright.sync_api import expect, Page

@allure.title("Add new place to the system")
@allure.description("""
Test Steps:
1. Navigate to add place page
2. Fill in place name in Arabic and English
3. Fill in place details/description in both languages
4. Select place category
5. Set place location coordinates
6. Upload place images (optional)
7. Submit the place information
8. Verify place is added successfully

This test validates the place addition functionality for citizen users.
""")
@allure.severity(allure.severity_level.NORMAL)
@scenario('../../features/citizen-features/add_place.feature', 'Successful place addition using valid data')
def test_add_place():
    pass


@when("I fill in the add place form with valid data")
def fill_add_place_form(page: Page, _pytest_bdd_example):
    place_data = _pytest_bdd_example.copy()

    # --- dynamic names/descriptions for uniqueness ---
    ts = int(time.time())
    suffix = f"{ts}-{random.randint(1000,9999)}"

    place_data.setdefault("place_name_ar", f"مكان تلقائي {suffix}")
    place_data.setdefault("place_name_en", f"Auto Place {suffix}")
    place_data.setdefault("place_details_ar", f"تفاصيل المكان التجريبي {suffix}")
    place_data.setdefault("place_details_en", f"Test place details {suffix}")

    AddPlacePage(page).add_place(place_data)

@then("the place should be submitted successfully")
def verify_place_submit_success(page: Page):
    expect(page.get_by_role("button", name="okay")).to_be_visible()
    page.get_by_role("button", name="okay").click()
