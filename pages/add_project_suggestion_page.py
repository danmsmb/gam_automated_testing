import os
from playwright.sync_api import Page
from pages.base_page import BasePage

class AddProjectSuggestionPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Navigation elements
        self.projects_nav = page.get_by_role("switch", name="NavItem.Projects")
        
        # Project filter buttons
        self.ongoing_filter = page.get_by_role("button", name="Ongoing")
        
        # Project selection
        self.ongoing_project_details_button = page.get_by_role("button", name="View details...").first
        
        # Project details page elements
        self.back_button = page.get_by_role("button", name="Back")
        self.project_title = page.locator("generic").first
        
        # Suggestion form elements
        self.suggestion_textbox = page.get_by_role("textbox", name="Add your suggestion... Write your suggestion...")
        self.send_button = page.get_by_role("button", name="Send")
        
        # Success confirmation
        self.success_dialog_ok_button = page.get_by_role("button", name="okay")
        
    def navigate_to_projects(self):
        """Navigate to projects page"""
        self.projects_nav.click()

    def filter_ongoing_projects(self):
        """Filter to show only ongoing projects"""
        self.ongoing_filter.click()

    def click_first_ongoing_project(self):
        """Click on the first ongoing project to view details"""
        self.ongoing_project_details_button.click()

    def fill_suggestion(self, suggestion_text: str):
        """Fill the suggestion text field"""
        self.suggestion_textbox.scroll_into_view_if_needed()
        self.suggestion_textbox.click()
        self.suggestion_textbox.fill(suggestion_text)
        # Give the form a moment to update
        self.page.wait_for_timeout(1000)

    def click_send_suggestion(self):
        """Click the send button to submit suggestion"""
        self.send_button.click()

    def click_success_ok(self):
        """Click OK on the success dialog"""
        self.success_dialog_ok_button.click()

    def wait_for_success_dialog(self):
        """Wait for the success dialog to appear"""
        self.success_dialog_ok_button.wait_for(state="visible", timeout=10000)

    def add_project_suggestion(self, suggestion_data: dict):
        """Complete project suggestion addition with provided data"""
        self.navigate_to_projects()
        self.page.wait_for_timeout(2000)  # Wait for projects to load

        self.filter_ongoing_projects()
        
        self.click_first_ongoing_project()
        self.page.wait_for_timeout(2000)  # Wait for project details to load
        
        # Add suggestion
        self.fill_suggestion(suggestion_data["suggestion_text"])
        self.click_send_suggestion()
        
        # Handle success dialog
        self.wait_for_success_dialog()
        self.click_success_ok()

    def is_suggestion_success_visible(self):
        """Check if the success dialog is visible"""
        return self.success_dialog_ok_button.is_visible()
