# tests/step_definitions/test_citizen_filter.py
import allure
import os
from pytest_bdd import scenario, scenarios, given, when, then
from pages.citizen_filter_page import CitizenFilterPage
import pytest, random, time
from playwright.sync_api import expect, Page

@allure.title("Filter events by wheelchair accessibility")
@allure.description("""
Test Steps:
1. Login as citizen
2. Navigate to main page with events
3. Click filter icon to open filter dialog
4. Select wheelchair accessibility filter
5. Apply filters
6. Verify filtered events are displayed
7. Check multiple event details to confirm wheelchair accessibility
8. Verify all events show wheelchair accessibility features

This test validates that the citizen filter functionality correctly filters events by wheelchair accessibility.
""")
@allure.severity(allure.severity_level.NORMAL)

@scenario('../features/citizen_filter.feature', 'Filter events by wheelchair accessibility and verify results')
def test_citizen_filter_wheelchair():
    pass

@when("I open the filter dialog and select wheelchair accessibility")
def open_filter_and_select_wheelchair(page: Page):
    """Open filter dialog and select wheelchair accessibility option"""
    filter_page = CitizenFilterPage(page)
    
    # Wait for page to load completely
    filter_page.wait_for_page_load()
    
    # Store the initial event count for comparison
    page.initial_event_count = filter_page.get_event_count()
    
    # Open filter dialog
    filter_page.open_filter_dialog()
    
    # Select wheelchair accessibility filter
    filter_page.select_wheelchair_filter()

@when("I apply the filters")
def apply_filters(page: Page):
    """Apply the selected filters"""
    filter_page = CitizenFilterPage(page)
    
    # Apply the filters
    filter_page.apply_filters()
    
    # Store the filtered event count
    page.filtered_event_count = filter_page.get_event_count()

@then("I should see filtered events")
def verify_filtered_events_displayed(page: Page):
    """Verify that filtered events are displayed"""
    filter_page = CitizenFilterPage(page)
    
    # Verify that events are still displayed after filtering
    expect(filter_page.events_section).to_be_visible()
    
    # Verify that we have at least one event showing
    current_event_count = filter_page.get_event_count()
    assert current_event_count > 0, "No events found after applying wheelchair accessibility filter"
    
    # Store event count for verification steps
    page.final_event_count = current_event_count

@when("I view details of multiple events")
def view_multiple_event_details(page: Page):
    """View details of multiple events to verify accessibility"""
    filter_page = CitizenFilterPage(page)
    
    # Store accessibility verification results
    page.wheelchair_accessibility_verified = []
    
    # Check up to 3 events or all available events if less than 3
    events_to_check = min(3, page.final_event_count)
    
    for i in range(events_to_check):
        # Click on event details
        filter_page.click_event_details(i)
        
        # Verify wheelchair accessibility is shown
        has_wheelchair_accessibility = filter_page.verify_wheelchair_accessibility()
        page.wheelchair_accessibility_verified.append(has_wheelchair_accessibility)
        
        # Go back to main page for next event
        if i < events_to_check - 1:  # Don't go back after the last event
            filter_page.go_back_to_main_page()

@then("all events should show wheelchair accessibility")
def verify_all_events_have_wheelchair_accessibility(page: Page):
    """Verify that all checked events show wheelchair accessibility"""
    
    # Ensure we have verification results
    assert hasattr(page, 'wheelchair_accessibility_verified'), "No accessibility verification results found"
    assert len(page.wheelchair_accessibility_verified) > 0, "No events were checked for accessibility"
    
    # Verify all events have wheelchair accessibility
    for i, has_accessibility in enumerate(page.wheelchair_accessibility_verified):
        assert has_accessibility, f"Event {i+1} does not show wheelchair accessibility"
    
    # Log successful verification
    events_checked = len(page.wheelchair_accessibility_verified)
    allure.attach(
        f"Successfully verified wheelchair accessibility in {events_checked} events",
        name="Verification Summary",
        attachment_type=allure.attachment_type.TEXT
    )