import pytest
import allure
from pytest_bdd import given, scenarios, when, then, parsers, scenario
from pages.login_page import LoginPage
from pages.event_search_page import EventSearchPage
import json


@allure.title("Event search functionality validation")
@allure.description("""
Test Steps:
1. Search for an existing event by name/location
2. Verify event appears in search results
3. Search for a non-existing event
4. Verify "no events found" message is displayed

This test validates the event search functionality for both existing and non-existing events.
""")
@allure.severity(allure.severity_level.CRITICAL)
@scenario('../../features/citizen-features/event_search.feature', 'Search for existing and non-existing events')
def test_event_search():
    pass


@when(parsers.parse('I search for an existing event "{search_term}"'))
def when_search_existing_event(page, search_term):
    search_page = EventSearchPage(page)
    search_page.search_for_event(search_term)


@then('I should see the event in the search results')
def then_see_event_results(page):
    search_page = EventSearchPage(page)
    # We know "test-location" is the search term from the feature file
    search_page.verify_event_found("test-location")


@when(parsers.parse('I search for a non-existing event "{search_term}"'))
def when_search_non_existing_event(page, search_term):
    search_page = EventSearchPage(page)
    search_page.search_for_event(search_term)


@then('I should see the no events message')
def then_see_no_events_message(page):
    search_page = EventSearchPage(page)
    search_page.verify_no_events_message()


@pytest.fixture(scope="session")
def config():
    with open("config.json", "r") as f:
        return json.load(f)
