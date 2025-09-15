import os
from playwright.sync_api import Page
from pages.base_page import BasePage

class AddPlacePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Navigation elements
        self.map_nav_button = page.get_by_role("switch", name="NavItem.Map")
        self.add_place_fab_button =   page.get_by_role("button", name="add_place_fab")
        self.add_place_option_button = page.get_by_text("Add Place")
        
        # Form elements
        self.place_name_ar_input = page.get_by_role("textbox", name="Enter suggested place name in Arabic...")
        self.place_name_en_input = page.get_by_role("textbox", name="Enter suggested place name in English...")
        self.place_category_dropdown = page.get_by_role("button", name="Enter location...")
        self.place_details_ar_input = page.get_by_role("textbox", name="Enter place details in Arabic...")
        self.place_details_en_input = page.get_by_role("textbox", name="Enter place details in English...")
        self.location_input = page.get_by_role("textbox", name="Enter location...")
        self.submit_button = page.get_by_role("button", name="Submit", exact=True)
        
        # Category options (common ones)
      
        self.mall_category_option = page.get_by_text("Mall")
        
        
        # Success confirmation
        self.ok_button = page.get_by_role("button", name="okay")

    def navigate_to_map(self):
        """Navigate to the map view"""
        self.map_nav_button.click()

    def click_add_place_fab(self):
        """Click the floating action button for adding place"""
        self.add_place_fab_button.click()

    def click_add_place_option(self):
        """Click the add place option from the bottom sheet"""
        self.add_place_option_button.click()

    def fill_place_name_ar(self, name_ar: str):
        """Fill the place name in Arabic"""
        self.place_name_ar_input.click()
        self.place_name_ar_input.fill(name_ar)

    def fill_place_name_en(self, name_en: str):
        """Fill the place name in English"""
        self.place_name_en_input.click()
        self.place_name_en_input.fill(name_en)

    def select_place_category(self):
        """Select place category from dropdown"""
        self.place_category_dropdown.click()
        self.mall_category_option.click()

    def fill_place_details_ar(self, details_ar: str):
        """Fill place details in Arabic"""
        self.place_details_ar_input.click()
        self.place_details_ar_input.fill(details_ar)

    def fill_place_details_en(self, details_en: str):
        """Fill place details in English"""
        self.place_details_en_input.click()
        self.place_details_en_input.fill(details_en)

    def fill_location(self):
        """Fill location field"""
        self.location_input.click()
        self.page.get_by_role("button", name="Accept", exact=True).click()

    def click_submit(self):
        """Click submit button"""
        self.submit_button.click()

    def click_ok_confirmation(self):
        """Click OK on success confirmation"""
        self.ok_button.click()

    def add_place(self, place_data: dict):
        """Complete place addition with provided data"""
        self.page.wait_for_timeout(5000)
        self.navigate_to_map()
        self.page.wait_for_timeout(5000)
        self.click_add_place_fab()
        self.click_add_place_option()
        self.fill_place_name_ar(place_data["place_name_ar"])
        self.fill_place_name_en(place_data["place_name_en"])
        self.select_place_category()
        self.fill_place_details_ar(place_data["place_details_ar"])
        self.fill_place_details_en(place_data["place_details_en"])
        self.fill_location()
        self.click_submit()
