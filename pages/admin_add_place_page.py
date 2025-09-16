"""
Page Object Model for Admin Add Place functionality.
This page handles admin-specific navigation to add places and reuses the existing AddPlacePage form.
"""

from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.add_place_page import AddPlacePage


class AdminAddPlacePage(BasePage):
    """Page object for admin add place functionality - handles admin-specific navigation."""
    
    def __init__(self, page: Page):
        """Initialize the AdminAddPlacePage with a Playwright page instance."""
        super().__init__(page)
        
        # Initialize the existing add place page for form handling
        self.add_place_page = AddPlacePage(page)
        
        # Admin-specific navigation selectors
        self.map_nav = page.get_by_text("Map")
        self.add_new_place_button = page.get_by_text("Add New Place")

        self.save_button = page.get_by_role("button", name="Save")
        
    def navigate_to_map(self):
        """Navigate to the Map section from admin side menu."""
        self.map_nav.click()
        self.page.wait_for_timeout(3000)
        
    def click_add_new_place(self):
        """Click the Add New Place button from admin map interface."""
        self.add_new_place_button.click()
        self.page.wait_for_timeout(3000)
        
    def add_place_admin_flow(self, place_data: dict):
        """Complete admin add place flow using existing add place form."""
        # Navigate to add place form via admin interface
        self.navigate_to_map()
        self.click_add_new_place()
        self.page.wait_for_timeout(1000)  # Allow time for any dynamic updates
        # Use existing add place page methods for form handling
        self.add_place_page.fill_place_name_ar(place_data["place_name_ar"])
        self.page.wait_for_timeout(1000)  # Allow time for any dynamic updates
        self.add_place_page.fill_place_name_en(place_data["place_name_en"])
        self.page.wait_for_timeout(1000)  # Allow time for any dynamic updates
        self.add_place_page.select_place_category()
        self.page.wait_for_timeout(1000)  # Allow time for any dynamic updates
        self.add_place_page.fill_place_details_ar(place_data["place_details_ar"])
        self.page.wait_for_timeout(1000)  # Allow time for any dynamic updates
        self.add_place_page.fill_place_details_en(place_data["place_details_en"])
        self.page.wait_for_timeout(1000)  # Allow time for any dynamic updates
        self.add_place_page.fill_location()
        self.page.wait_for_timeout(1000)  # Allow time for any dynamic updates
        self.save_button.click()
        
    def get_current_page_url(self) -> str:
        """Get the current page URL."""
        return self.page.url