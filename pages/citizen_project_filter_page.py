from playwright.sync_api import Page
from pages.base_page import BasePage
import time

class CitizenProjectFilterPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Navigation elements
        self.projects_nav = page.get_by_role("switch", name="NavItem.Projects")
        
        # Filter elements
        self.planned_filter_button = page.get_by_role("button", name="Planned", exact=True)
        self.ongoing_filter_button = page.get_by_role("button", name="Ongoing", exact=True)
        self.completed_filter_button = page.get_by_role("button", name="Completed", exact=True)
        
        # Project elements
        self.search_textbox = page.get_by_role("textbox", name="Search Projects")
        self.view_details_buttons = page.get_by_role("button", name="View details...")
        
        # Project status labels
        self.planned_status_labels = page.get_by_role("button", name="project_status_planned")
        self.ongoing_status_labels = page.get_by_role("button", name="project_status_ongoing")
        self.completed_status_labels = page.get_by_role("button", name="project_status_completed")
        
    def load(self, config):
        """Navigate to citizen main page"""
        self.page.goto(config['app_home_page_url'])
        
    def navigate_to_projects(self):
        """Navigate to the projects section"""
        self.projects_nav.click()
        # Wait for projects page to load
        self.search_textbox.wait_for(timeout=10000)
        time.sleep(2)  # Allow page to fully load
        
    def filter_by_planned(self):
        """Filter projects by planned status"""
        self.planned_filter_button.click()
        # Wait for filter to apply
        time.sleep(2)
        
    def filter_by_ongoing(self):
        """Filter projects by ongoing status"""
        self.ongoing_filter_button.click()
        # Wait for filter to apply
        time.sleep(2)
        
    def filter_by_completed(self):
        """Filter projects by completed status"""
        self.completed_filter_button.click()
        # Wait for filter to apply
        time.sleep(2)
        
    def get_planned_projects_count(self):
        """Get the number of projects with planned status"""
        return self.planned_status_labels.count()
        
    def get_ongoing_projects_count(self):
        """Get the number of projects with ongoing status"""
        return self.ongoing_status_labels.count()
        
    def get_completed_projects_count(self):
        """Get the number of projects with completed status"""
        return self.completed_status_labels.count()
        
    def get_total_projects_count(self):
        """Get the total number of projects displayed"""
        return self.view_details_buttons.count()
        
    def verify_all_projects_have_planned_status(self):
        """Verify that all visible projects have planned status"""
        total_projects = self.get_total_projects_count()
        planned_projects = self.get_planned_projects_count()
        return total_projects > 0 and total_projects == planned_projects
        
    def verify_all_projects_have_ongoing_status(self):
        """Verify that all visible projects have ongoing status"""
        total_projects = self.get_total_projects_count()
        ongoing_projects = self.get_ongoing_projects_count()
        return total_projects > 0 and total_projects == ongoing_projects
        
    def verify_all_projects_have_completed_status(self):
        """Verify that all visible projects have completed status"""
        total_projects = self.get_total_projects_count()
        completed_projects = self.get_completed_projects_count()
        return total_projects > 0 and total_projects == completed_projects
        
    def is_planned_filter_active(self):
        """Check if planned filter button is active"""
        try:
            # Check if the planned button has the active attribute
            planned_button = self.page.locator('button:has-text("Planned"):has([active])')
            return planned_button.count() > 0
        except:
            return False
            
    def is_ongoing_filter_active(self):
        """Check if ongoing filter button is active"""
        try:
            # Check if the ongoing button has the active attribute
            ongoing_button = self.page.locator('button:has-text("Ongoing"):has([active])')
            return ongoing_button.count() > 0
        except:
            return False
            
    def is_completed_filter_active(self):
        """Check if completed filter button is active"""
        try:
            # Check if the completed button has the active attribute
            completed_button = self.page.locator('button:has-text("Completed"):has([active])')
            return completed_button.count() > 0
        except:
            return False
            
    def get_project_status_summary(self):
        """Get a summary of project statuses for debugging"""
        return {
            'total_projects': self.get_total_projects_count(),
            'planned_projects': self.get_planned_projects_count(),
            'ongoing_projects': self.get_ongoing_projects_count(),
            'completed_projects': self.get_completed_projects_count()
        }