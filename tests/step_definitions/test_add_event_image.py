# tests/step_definitions/test_add_event_image.py
import allure
import os
from pytest_bdd import scenario, scenarios, given, when, then
from pages.add_event_image_page import AddEventImagePage
import pytest, random, time
from playwright.sync_api import expect, Page

@allure.title("Add image to event")
@allure.description("""
Test Steps:
1. Navigate to events page
2. Select an event and view details
3. Click Add Image button
4. Choose and upload a valid image file
5. Click Add Images to submit
6. Verify Done button appears
7. Click Done to complete the process

This test validates the event image upload functionality for citizen users.
""")
@allure.severity(allure.severity_level.NORMAL)

@scenario('../features/add_event_image.feature', 'Successful event image addition using valid image file')
def test_event_image():
    pass

@when("I navigate to event details and add an image with valid data")
def add_event_image_with_valid_data(page: Page, _pytest_bdd_example):
    image_data = _pytest_bdd_example.copy()

    # Set up the image path - use the test image from resources folder
    image_data.setdefault("image_path", "resources/images/Screenshot 2024-11-11 143744.png")

    # Store reference for verification
    page.image_upload_completed = False

    add_image_page = AddEventImagePage(page)
    
    # Navigate to event and open add image dialog
    add_image_page.page.wait_for_timeout(5000)
    add_image_page.click_view_details()
    add_image_page.page.wait_for_timeout(3000)
    add_image_page.click_add_image()
    add_image_page.page.wait_for_timeout(2000)
    
    # Handle file upload
    absolute_image_path = os.path.abspath(image_data["image_path"])
    
    # Set up file chooser handler before clicking the button
    with page.expect_file_chooser() as fc_info:
        add_image_page.click_choose_images()
    file_chooser = fc_info.value
    file_chooser.set_files(absolute_image_path)
    
    # Wait for file to be processed
    page.wait_for_timeout(2000)
    
    # Click add images to submit
    add_image_page.click_add_images()
    page.wait_for_timeout(3000)
    
    # Mark as completed for verification
    page.image_upload_completed = True


@then("the Done button should be visible")
def verify_done_button_visible(page: Page):
    """Verify that the Done button is visible after successful upload."""
    add_image_page = AddEventImagePage(page)
    
    # Wait for Done button to appear
    add_image_page.wait_for_done_button()
    
    # Verify Done button is visible
    expect(add_image_page.done_button).to_be_visible()
    
    # Click Done to complete the flow
    add_image_page.click_done()
    page.wait_for_timeout(2000)