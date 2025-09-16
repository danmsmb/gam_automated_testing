import os
from playwright.sync_api import Page
from tests.step_definitions.conftest import config
from pages.base_page import BasePage

class AdminSurveyFilterPage(BasePage):
    """Page object for admin survey filter template creation"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Menu navigation
        self.survey_filter_templates_menu = page.get_by_text("Survey Filter Templates")
        
        # Survey filter template page elements
        self.create_new_template_button = page.get_by_role("button", name="Create New Survey Template")
        
        # Form elements
        self.target_group_name_input = page.get_by_role("textbox", name="Enter target group name")
        self.location_button = page.get_by_role("button", name="Enter location...")
        self.bader_location_option = page.get_by_text("Bader", exact=True)
        
        # Gender options
        self.male_gender = page.get_by_text("Male", exact=True)
        self.female_gender = page.get_by_text("Female", exact=True)
        self.all_gender = page.get_by_text("All", exact=True)
        
        # Age sliders (keep as is per requirement)
        self.min_age_slider = page.locator('slider').first
        self.max_age_slider = page.locator('slider').last
        
        # Submit button
        self.submit_button = page.get_by_role("button", name="Submit Survey Filter Template")
        
        # Success elements
        self.okay_button = page.get_by_role("button", name="okay")
       
        
    def navigate_to_survey_filter_templates(self):
        """Navigate to the survey filter templates section"""
        self.survey_filter_templates_menu.click()
        self.page.wait_for_timeout(2000)
        
    def click_create_new_template(self):
        """Click the create new survey template button"""
        self.create_new_template_button.click()
        self.page.wait_for_timeout(2000)
        
    def fill_target_group_name(self, name: str):
        """Fill the target group name input"""
        self.target_group_name_input.click()
        self.target_group_name_input.fill(name)
        self.page.wait_for_timeout(1000)
        
    def select_location(self):
        """Select Bader as the location"""
        self.location_button.click()
        self.page.wait_for_timeout(1000)
        self.bader_location_option.click()
        self.page.wait_for_timeout(1000)
        
    def select_gender_all(self):
        """Select 'All' for gender"""
        self.all_gender.click()
        self.page.wait_for_timeout(1000)
        
    def keep_age_sliders_as_is(self):
        """Keep the age sliders in their default position (as per requirement)"""
        # No action needed - requirement is to keep sliders as is
        pass
        
    def submit_template(self):
        """Submit the survey filter template"""
        self.submit_button.click()
        self.page.wait_for_timeout(3000)
        
    def verify_okay_button_visible(self) -> bool:
        """Verify that the okay button is visible (success confirmation)"""
        return self.okay_button.is_visible()
        
    def click_okay_button(self):
        """Click the okay button to close the success dialog"""
        self.okay_button.click()
        self.page.wait_for_timeout(2000)
        
    def create_survey_filter_template(self, template_name: str):
        """Complete the entire survey filter template creation flow"""
        # Step 1: Navigate to survey filter templates
        self.navigate_to_survey_filter_templates()
        
        # Step 2: Click create new template
        self.click_create_new_template()
        
        # Step 3: Fill form details
        self.fill_target_group_name(template_name)
        self.select_location()
        self.select_gender_all()
     
        
        # Step 4: Submit template
        self.submit_template()
        
        # Step 5: Verify success and close dialog
        is_success = self.verify_okay_button_visible()
        if is_success:
            self.click_okay_button()
            
        return is_success