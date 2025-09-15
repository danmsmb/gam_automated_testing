import os
from playwright.sync_api import Page
from pages.base_page import BasePage

class AddProjectFeedbackPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Navigation elements
        self.projects_nav = page.get_by_role("switch", name="NavItem.Projects")
        
        # Project filter buttons
        self.completed_filter = page.get_by_role("button", name="Completed")
        
        # Project selection - look for completed projects
        self.completed_project_details_button = page.get_by_role("button", name="View details...").first
        
        # Project details page elements
        self.back_button = page.get_by_role("button", name="Back")
        self.project_title = page.locator("generic").first
        
        # Feedback form elements
        self.feedback_textbox = page.get_by_role("textbox", name="What is the impact of this project on you?")
        self.send_button = page.get_by_role("button", name="Send")
        
        # Project rating elements (stars)
        self.rating_stars = page.locator("[role='img']").filter(has_text="")
        
        # Success confirmation
        self.success_dialog_ok_button = page.get_by_role("button", name="okay")
        
    def navigate_to_projects(self):
        """Navigate to projects page"""
        self.projects_nav.click()

    def filter_completed_projects(self):
        """Filter to show only completed projects"""
        self.completed_filter.click()

    def click_first_completed_project(self):
        """Click on the first completed project to view details"""
        self.completed_project_details_button.click()

    def fill_feedback(self, feedback_text: str):
        """Fill the feedback text field"""
        self.feedback_textbox.scroll_into_view_if_needed()
        self.feedback_textbox.click()
        self.feedback_textbox.fill(feedback_text)
        # Give the form a moment to update
        self.page.wait_for_timeout(1000)


    def click_send_feedback(self):
        """Click the send button to submit feedback"""
        self.send_button.click()

    def click_success_ok(self):
        """Click OK on the success dialog"""
        self.success_dialog_ok_button.click()

    def wait_for_success_dialog(self):
        """Wait for the success dialog to appear"""
        self.success_dialog_ok_button.wait_for(state="visible", timeout=10000)

    def add_project_feedback(self, feedback_data: dict):
        """Complete project feedback addition with provided data"""
        self.navigate_to_projects()
        self.page.wait_for_timeout(2000)  # Wait for projects to load

        self.filter_completed_projects()
        
        
        self.click_first_completed_project()
        self.page.wait_for_timeout(2000)  # Wait for project details to load
        
        # Add feedback
        self.fill_feedback(feedback_data["feedback_text"])
        self.click_send_feedback()
        
        # Handle success dialog
        self.wait_for_success_dialog()
        self.click_success_ok()

    def is_feedback_success_visible(self):
        """Check if the success dialog is visible"""
        return self.success_dialog_ok_button.is_visible()
