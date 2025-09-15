from playwright.sync_api import Page, expect


class EventSearchPage:
    def __init__(self, page: Page):
        self.page = page
        # Search-related locators
        self.search_input = page.get_by_role("textbox", name="Discover events near you....")
        self.view_details_button = page.get_by_role("button", name="View details...")
        self.back_button = page.get_by_role("button", name="Back")
        self.no_events_message = page.get_by_text("There appear to be no events at this time")
        
    def search_for_event(self, search_term: str):
        """Search for an event using the search box"""
        self.search_input.click()
        self.search_input.fill(search_term)
        self.page.wait_for_timeout(2000)  # Wait for search results to load
        
        
    def verify_event_found(self, event_name: str):
        """Verify that an event appears in the search results"""
        # Look for event cards that contain the searched event name
        self.view_details_button.first.click()
        self.page.wait_for_timeout(2000)
        expect(self.page.get_by_text(event_name, exact=True)).to_be_visible()
        self.back_button.click()
        self.page.reload()
        self.page.wait_for_timeout(2000)

    def verify_no_events_message(self):
        """Verify that the 'no events' message is displayed"""
        expect(self.no_events_message).to_be_visible()
        
    def verify_search_box_contains_text(self, text: str):
        """Verify that the search box contains the specified text"""
        expect(self.search_input).to_have_value(text)
