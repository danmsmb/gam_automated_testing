from playwright.sync_api import Page
from pages.base_page import BasePage
import time

class CitizenFilterPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Main page elements
        self.search_textbox = page.get_by_role("textbox", name="Discover events near you....")
        self.filter_icon = page.get_by_role("button", name="filter_icon")
        self.events_section = page.get_by_text("Upcoming Events / Active Events")
        
        # Filter dialog elements
        self.wheelchair_filter = page.get_by_role("button", name="Wheelchair")
        self.apply_filters_button = page.get_by_role("button", name="Apply Filters")
        self.accessibility_section = page.get_by_text("Accessibility")
        
        # Event elements
        self.view_details_buttons = page.get_by_role("button", name="View details...")
        self.back_button = page.get_by_role("button", name="Back")
        
        # Event details elements  
        self.event_accessibility_section = page.get_by_text("Accessibility")
        self.wheelchair_text = page.get_by_text("Wheelchair")
        
    def load(self, config):
        """Navigate to citizen main page"""
        self.page.goto(config['app_home_page_url'])
        
    def wait_for_page_load(self):
        """Wait for the main page to load"""
        self.search_textbox.wait_for(timeout=10000)
        self.events_section.wait_for(timeout=10000)
        
    def open_filter_dialog(self):
        """Click on the filter icon to open filter dialog"""
        self.filter_icon.click()
        # Wait for dialog to appear
        self.accessibility_section.wait_for(timeout=5000)
        
    def select_wheelchair_filter(self):
        """Select the wheelchair accessibility filter"""
        self.wheelchair_filter.click()
        # Wait a moment for selection to register
        time.sleep(1)
        
    def apply_filters(self):
        """Apply the selected filters"""
        self.apply_filters_button.click()
        # Wait for page to reload with filtered results
        time.sleep(2)
        
    def get_event_count(self):
        """Get the number of view details buttons (events) visible"""
        return self.view_details_buttons.count()
        
    def click_event_details(self, index: int):
        """Click on view details for event at given index (0-based)"""
        self.view_details_buttons.nth(index).click()
        # Wait for event details page to load
        self.back_button.wait_for(timeout=5000)
        
    def verify_wheelchair_accessibility(self):
        """Verify that wheelchair accessibility is shown in event details"""
        # Check that accessibility section exists
        self.event_accessibility_section.wait_for(timeout=5000)
        # Check that wheelchair text is visible
        return self.wheelchair_text.is_visible()
        
    def go_back_to_main_page(self):
        """Go back from event details to main page"""
        self.back_button.click()
        # Wait for main page to load
        self.events_section.wait_for(timeout=5000)
        
    def filter_events_by_wheelchair_accessibility(self):
        """Complete workflow to filter events by wheelchair accessibility"""
        self.open_filter_dialog()
        self.select_wheelchair_filter()
        self.apply_filters()