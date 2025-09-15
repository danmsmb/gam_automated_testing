# tests/step_definitions/test_suggest_event.py
import allure
from pytest_bdd import scenarios, given, when, then, scenario
from pages.suggest_event_page import SuggestEventPage
import pytest, random, time
from playwright.sync_api import expect, Page
from datetime import datetime, timedelta
import time, random

@allure.title("Citizen suggests a new event")
@allure.description("""
Test Steps:
1. Citizen navigates to suggest event page
2. Fill in event name in Arabic and English
3. Select start and end dates
4. Choose event location
5. Select event category
6. Choose accessibility options
7. Fill in event descriptions
8. Submit the event suggestion
9. Verify success message is displayed

This test validates the complete event suggestion flow for citizen users.
""")
@allure.severity(allure.severity_level.NORMAL)
@scenario('../features/suggest_event.feature', 'Successful event suggestion using valid data')
def test_suggest_event():
    pass
    pass


def _aria_date_label(d: datetime, today_flag: bool = False) -> str:
    """
    Build the aria-name that your calendar uses, e.g.:
      "Friday, September 12, 2025, Today"  (when today_flag=True)
      "Tuesday, September 16, 2025"
    """
    # Weekday/Month names come from system locale; if your app is always English,
    # run tests on an English locale machine.
    label = f"{d.strftime('%A')}, {d.strftime('%B')} {d.day}, {d.year}"
    if today_flag:
        label += ", Today"
    return label

@when("I fill in the suggest event form with valid data")
def fill_suggest_event_form(page: Page, _pytest_bdd_example):
    event_data = _pytest_bdd_example.copy()

    # --- dynamic names/descriptions for uniqueness ---
    ts = int(time.time())
    suffix = f"{ts}-{random.randint(1000,9999)}"

    event_data.setdefault("event_name_ar", f"فعالية تلقائية {suffix}")
    event_data.setdefault("event_name_en", f"Auto Event {suffix}")
    event_data.setdefault("event_description_ar", f"وصف الفعالية التجريبية {suffix}")
    event_data.setdefault("event_description_en", f"Test event description {suffix}")

    # --- dates: start = today, end = today + 4 days ---
    today = datetime.now()
    end = today + timedelta(days=4)

    event_data["start_date"] = _aria_date_label(today, today_flag=True)
    event_data["end_date"]   = _aria_date_label(end, today_flag=False)


    SuggestEventPage(page).suggest_event(event_data)

@then("the event should be submitted successfully")
def verify_event_submit_success(page: Page):
    expect(page.get_by_role("button", name="okay")).to_be_visible()
    page.get_by_role("button", name="okay").click()
