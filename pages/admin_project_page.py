from playwright.sync_api import Page
from pages.base_page import BasePage
import time

class AdminProjectPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Navigation
        self.strategic_projects_menu = page.get_by_text("Strategic Projects")
        self.add_new_project_button = page.get_by_role("button", name="Add New Project")
        
        # Form fields
        self.project_name_arabic = page.get_by_role("textbox", name="Enter project name in Arabic")
        self.project_name_english = page.get_by_role("textbox", name="Enter project name in English")
        self.description_arabic = page.get_by_role("textbox", name="Write project description in Arabic")
        self.description_english = page.get_by_role("textbox", name="Write project description in English")
        self.partners_textbox = page.get_by_role("textbox", name="Enter Project Partners")
        self.start_date_textbox = page.get_by_role("textbox", name="Enter planned start date")
        
        # Dropdowns
        self.sections_dropdown = page.get_by_role("button", name="sections")
        self.goals_dropdown = page.get_by_role("button", name="goals")
        self.strategic_objectives_dropdown = page.get_by_role("button", name="strategic_objectives")
        self.status_dropdown = page.get_by_role("button", name="Select project status")
        
        # Dropdown options
        self.planning_section_checkbox = page.get_by_role("checkbox", name="Planning and Economic")
        self.urban_planning_goal_checkbox = page.get_by_role("checkbox", name="Comprehensive and Sustainable")
        self.balance_objective_checkbox = page.get_by_role("checkbox", name="Achieving balance in urban")
        self.planned_status_option = page.get_by_text("Planned")
        self.apply_button = page.get_by_role("button", name="Apply")
        
        # Date picker
        self.date_picker_ok_button = page.get_by_role("button", name="OK")
        
        # Form actions
        self.save_button = page.get_by_role("button", name="Save")
        self.success_ok_button = page.get_by_role("button", name="okay")
        
    def navigate_to_projects(self):
        """Navigate to Strategic Projects section"""
        self.strategic_projects_menu.click()
        time.sleep(2)
        
    def create_project(self, project_data: dict):
        """Create a new project with the provided data"""
        self.add_new_project_button.click()
        time.sleep(1)
        
        # Fill project names
        self.project_name_arabic.click()
        self.project_name_arabic.fill(project_data["name_arabic"])
        self.page.wait_for_timeout(1000)
        self.project_name_english.click()
        self.project_name_english.fill(project_data["name_english"])

        self.page.wait_for_timeout(1000)
        
        # Select sections
        self.sections_dropdown.click()
        self.planning_section_checkbox.click()
        self.apply_button.click()

        self.page.wait_for_timeout(1000)
        # Select goals
        self.goals_dropdown.click()
        self.urban_planning_goal_checkbox.click()
        self.apply_button.click()

        self.page.wait_for_timeout(1000)
        
        # Select strategic objectives
        self.strategic_objectives_dropdown.click()
        self.balance_objective_checkbox.click()
        self.apply_button.click()

        self.page.wait_for_timeout(1000)
        
        # Select status
        self.status_dropdown.click()
        self.planned_status_option.click()

        self.page.wait_for_timeout(1000)
        
        # Fill descriptions
        self.description_arabic.click()
        self.description_arabic.fill(project_data["description_arabic"])
        self.page.wait_for_timeout(1000)
        self.description_english.click()
        self.description_english.fill(project_data["description_english"])
        self.page.wait_for_timeout(1000)

        
        # Set start date using date picker
        self.start_date_textbox.click()
        self.page.get_by_role("button", name=project_data["start_date"]).click()
        self.date_picker_ok_button.click()
        self.page.wait_for_timeout(1000)
        
        # Fill partners
        self.partners_textbox.click()
        self.partners_textbox.fill(project_data["partners"])

        self.page.wait_for_timeout(1000)
        
        # Save project
        self.save_button.click()
        time.sleep(2)
        
        # Handle success dialog
        self.success_ok_button.click()
        time.sleep(1)