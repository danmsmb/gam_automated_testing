import os
import re
from playwright.sync_api import Page
from tests.step_definitions.conftest import config
from pages.base_page import BasePage

class CitizenSurveyPage(BasePage):
    """Page object for citizen survey interactions"""
    
    def __init__(self, page: Page):
        super().__init__(page)

        # Navigation selectors
        self.surveys_nav = page.get_by_role("switch", name="NavItem.Surveys")
        
        # Survey list selectors
        self.first_survey = page.get_by_role("button", name=re.compile("survey_card_")).first
        # Survey form selectors
        self.survey_title = page.get_by_text("Test Survey - Automated")
        self.survey_text_input = page.get_by_role("textbox", name="What are your thoughts on the")
        self.send_button = page.get_by_role("button", name="Send")
        self.back_button = page.get_by_role("button", name="Back")
        
        # Success and validation selectors
      
        self.okay_button = page.get_by_role("button", name="okay")
        self.already_submitted_message = page.get_by_text("You have already submitted")
        self.go_back_button = page.get_by_role("button", name="Go Back")
        
        
    def navigate_to_surveys(self):
        """Navigate to the surveys section from citizen main page"""
        self.surveys_nav.click()
        self.page.wait_for_timeout(3000)
        
    def click_first_survey(self):
        """Click on the first survey in the list"""
        self.first_survey.click()
        self.page.wait_for_timeout(2000)
        
    def fill_survey_form(self, response_text: str):
        """Fill out the survey form with the provided response"""
        self.survey_text_input.click()
        self.survey_text_input.fill(response_text)
        self.page.wait_for_timeout(1000)
        
    def submit_survey(self):
        """Submit the survey form"""
        self.send_button.click()
        self.page.wait_for_timeout(2000)
        
    def confirm_submission(self):
        """Confirm the survey submission by clicking okay"""
        self.okay_button.click()
        self.page.wait_for_timeout(2000)
    
    def click_back(self):
        """Click the back button to return to survey list"""
        self.back_button.click()
        self.page.wait_for_timeout(2000)
            
    def verify_already_submitted_message(self) -> bool:
        """Verify that the 'already submitted' message is displayed"""
        return self.already_submitted_message.is_visible()
            
    def click_go_back(self):
        """Click the go back button from already submitted screen"""
        self.go_back_button.click()
        self.page.wait_for_timeout(2000)
        
    def complete_citizen_survey_flow(self, username: str, password: str, response_text: str):
        """Complete the entire citizen survey flow"""
       
        # Step 2: Navigate to surveys
        self.navigate_to_surveys()
        
        # Step 3: Fill and submit survey
        self.click_first_survey()
        self.fill_survey_form(response_text)
        self.submit_survey()
        self.confirm_submission()


        
        # Step 4: Verify already submitted message
        self.click_first_survey()
        is_already_submitted = self.verify_already_submitted_message()
        self.click_go_back()
        
        return is_already_submitted