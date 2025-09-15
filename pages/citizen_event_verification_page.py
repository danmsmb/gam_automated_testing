from playwright.sync_api import Page, expect
from pages.event_search_page import EventSearchPage


class CitizenEventVerificationPage(EventSearchPage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Citizen-specific locators
        self.upcoming_events_section = page.get_by_text("Upcoming Events / Active Events")
        self.past_events_section = page.get_by_text("Past Events")
        self.event_view_details_button = page.get_by_role("button", name="View details...")
        
        
    def search_and_verify_event(self, event_name: str):
        """Search for event and verify it appears in results (reuses EventSearchPage)"""
        self.search_for_event(event_name)
        self.verify_event_found(event_name)
        