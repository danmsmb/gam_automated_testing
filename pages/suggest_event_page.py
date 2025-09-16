import os
from playwright.sync_api import Page
from tests.step_definitions.conftest import config
from pages.base_page import BasePage

class SuggestEventPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.suggest_event_plus_btn = page.get_by_role("button", name="suggestNewEvent")
        self.suggest_new_event_button =  page.get_by_text("Suggest a new event")
        self.suggested_event_name_ar_input = page.get_by_role("textbox", name="Enter suggested event name in Arabic...")
        self.suggested_event_name_en_input = page.get_by_role("textbox", name="Enter suggested event name in English...")
        self.start_date_input = page.get_by_role("textbox", name="Enter date...").first
        self.date_ok_button = page.get_by_role("button", name="OK")
        self.end_date_input = page.get_by_role("textbox", name="Enter date...").last
        self.end_date_time = page.get_by_role("button", name="Sunday, September 14, 2025")
        self.location_list = page.get_by_role("button", name="Enter location...")
        self.location_option =  page.get_by_text("Bader", exact=True)
        self.event_category_list = page.get_by_text("Enter event category...")
        self.event_category_option = page.get_by_role("button", name="Sport")
        self.event_description_input_ar = page.get_by_role("textbox", name="Write event description in")
        self.event_description_input_en = page.get_by_role("textbox", name="Write a description for the")
        self.submit_button = page.get_by_role("button", name="Send Suggestion")
        self.ok_button = page.get_by_role("button", name="okay")
        self.event_accessibility_list = page.get_by_text("Enter event accessibility...")
        self.electrical_stairs_option = page.get_by_role("button", name="Electrical Stairs")
        self.done_button = page.get_by_role("button", name="Done")

    def suggest_event(self, event_data: dict):
        self.suggest_event_plus_btn.click()
        self.suggest_new_event_button.click()
        self.page.wait_for_timeout(1000)
        self.location_list.click()
        self.page.wait_for_timeout(1000)
        self.location_option.click()
        self.page.wait_for_timeout(1000)
        self.suggested_event_name_ar_input.click()
        self.suggested_event_name_ar_input.fill(event_data["event_name_ar"])
        self.page.wait_for_timeout(1000)
        self.suggested_event_name_en_input.click()
        self.suggested_event_name_en_input.fill(event_data["event_name_en"])
        self.page.wait_for_timeout(1000)
        self.start_date_input.click()
        self.page.get_by_role("button", name=event_data["start_date"]).click()
        self.date_ok_button.click()
        self.date_ok_button.click()
        self.end_date_input.click()
        self.page.get_by_role("button", name=event_data["end_date"]).click()
        self.date_ok_button.click()
        self.date_ok_button.click()
        
        self.page.wait_for_timeout(1000)
        self.event_category_list.click()
        self.event_category_option.click()
        self.done_button.click()
        self.page.wait_for_timeout(1000)
        self.event_accessibility_list.click()
        self.electrical_stairs_option.click()
        self.done_button.click()
        self.page.wait_for_timeout(2000)
        self.event_description_input_ar.click()
        self.event_description_input_ar.fill(event_data["event_description_ar"])
        self.page.wait_for_timeout(2000)
        self.event_description_input_en.click()
        self.event_description_input_en.fill(event_data["event_description_en"])
        self.page.wait_for_timeout(1000)
        self.submit_button.click()
        