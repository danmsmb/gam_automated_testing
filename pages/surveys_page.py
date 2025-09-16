# pages/surveys_page.py
import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import time, random
from datetime import datetime
from pages.login_page import LoginPage
from tests.step_definitions.conftest import page

class SurveysPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Navigation elements
        self.surveys_menu = page.get_by_text("Surveys")
        self.create_survey_button = page.get_by_role("button", name="Create New Survey")
        
        # Survey form elements
        self.survey_title_input = page.get_by_role("textbox", name="Title")
        self.survey_description_textarea = page.get_by_role("textbox", name="Description")
        self.start_date_input = page.get_by_role("textbox", name="Start Date")
        self.end_date_input = page.get_by_role("textbox", name="End Date")
        self.survey_type_list = page.get_by_role("combobox", name="Form Type").locator("span")
        self.survey_option = page.get_by_text("Survey")
        self.add_section_button = page.get_by_role("heading", name="Add Section")
        self.add_question_button = page.get_by_role("button", name="")
        self.add_question = page.locator("#section-content-0").get_by_role("button").first
        self.question_text_input = page.get_by_role("textbox", name="Question")
        self.answer_type_list = page.get_by_role("combobox", name="Answer Type").get_by_role("img")
        self.long_text_option = page.get_by_text("Long Text")
        self.save_question = page.locator("#question-0").get_by_role("button", name="Save")

        
        # Action buttons
        self.save_button = page.get_by_role("button", name="Save")
        self.publish_button = page.get_by_role("button", name="Publish")
        self.enable_button = page.get_by_role("button", name="Enable")
        self.submit_filter_button = page.get_by_role("button", name="Submit Filter")
        self.okay_button = page.get_by_role("button", name="okay")
        
    def click_surveys_menu(self):
        self.page.get_by_text("Surveys").click()

    def navigate_to_surveys(self):
        
        self.page.get_by_role("textbox", name="Username").fill("omar")
        self.page.get_by_role("textbox", name="Password").fill("Admin@pass123")
        self.page.get_by_role("button", name="Login").click()
        self.page.wait_for_timeout(3000)
        self.page.get_by_role("navigation").get_by_role("button").filter(has_text=re.compile(r"^$")).click()
        self.page.get_by_text("Forms").first.click()
        self.page.get_by_text("Forms").nth(1).click()
        self.page.get_by_role("button", name="Create Form").click()

        

    def click_create_survey(self):
        """Click the Create New Survey button"""
        # Store current page count
        current_pages = len(self.page.context.pages)
        
        self.create_survey_button.click()
        
        # Wait for new page to open
        self.page.wait_for_timeout(3000)
        
        # Switch to the new tab if one was opened
        if len(self.page.context.pages) > current_pages:
            new_page = self.page.context.pages[-1]  # Get the latest page
            self.page = new_page  # Update the page reference
            self.page.wait_for_load_state('domcontentloaded')
            self.page.wait_for_timeout(2000)

    def fill_survey_basic_info(self, survey_data: dict):
        """Fill the basic survey information"""
        # Fill survey title
        self.survey_title_input.click()
        self.survey_title_input.fill(survey_data["title"])
        self.page.wait_for_timeout(1000)
        
        self.survey_type_list.click()
        self.page.wait_for_timeout(500)
        self.survey_option.click()
        # Fill survey description
        self.survey_description_textarea.click()
        self.survey_description_textarea.fill(survey_data["description"])
        self.page.wait_for_timeout(1000)
        # Set start date to today
        self.page.locator("mat-form-field").filter(has_text="Start DateDD/MM/YYYY").get_by_label("Open calendar").click()
        self. page.get_by_role("button", name="15/09/").click()
        self.page.wait_for_timeout(1000)
        self.page.locator("mat-form-field").filter(has_text="End DateDD/MM/YYYY").get_by_label("Open calendar").click()
        self.page.get_by_role("button", name="30/09/").click()

        
    def save_survey(self):
        """Save the survey"""
        self.save_button.click()
        self.page.wait_for_timeout(3000)  # Wait for save to complete

    def add_long_text_question(self, question_text: str):
        """Add a long text question to the survey"""
        # Click Add Question
        self.add_section_button.click()
        self.page.wait_for_timeout(1000)

        self.add_question_button.click()
        self.page.wait_for_timeout(1000)

        self.add_question.click()
        self.page.wait_for_timeout(1000)

        self.question_text_input.fill(question_text)
        self.page.wait_for_timeout(500)
        
        self.answer_type_list.click()
        self.page.wait_for_timeout(500)
        
        # Select Long Text option
        self.long_text_option.click()
        self.page.wait_for_timeout(500)
        
        # Save the question
        self.save_question.click()
        self.page.wait_for_timeout(2000)

    def publish_survey(self):
        """Publish the survey"""
        self.publish_button.click()
        self.page.wait_for_timeout(3000)

    def enable_survey(self):
        """Enable the survey"""
        self.enable_button.click()
        self.page.wait_for_timeout(3000)

    def navigate_to_main_app(self, page: Page, config):
        """Navigate back to the main application"""
        # Navigate to the main app URL
        self.page.goto("https://gamail.dev.internal.sirenanalytics.com/gamail_web/login")
        LoginPage(page).login('admin', config)
        self.page.wait_for_timeout(3000)

    def find_and_click_created_survey(self, survey_title: str):
        """Find and click on the created survey"""
        # Go to Surveys section
        self.click_surveys_menu()
        
        # Look for the survey by title and click it
        survey_element = self.page.get_by_role("button", name=re.compile("survey_card_")).first
        survey_element.click()
        self.page.wait_for_timeout(5000)

    def submit_survey_filter(self):
        """Submit the survey filter"""
        self.submit_filter_button.click()
        self.page.wait_for_timeout(40000)  # Wait for processing

    def wait_for_success_message(self):
        """Wait for and verify the success message appears"""
  
        expect(self.okay_button).to_be_visible()

    def click_okay_on_success(self):
        """Click okay on the success dialog"""
        self.okay_button.click()
        self.page.wait_for_timeout(2000)

    def create_complete_survey(self, survey_data: dict, question_text: str):
        """Complete survey creation flow"""
        self.navigate_to_surveys()
        self.click_create_survey()
        self.fill_survey_basic_info(survey_data)
        self.save_survey()
        self.add_long_text_question(question_text)
        self.publish_survey()
        self.enable_survey()

    def submit_survey_as_admin(self, survey_title: str):
        """Complete survey submission flow as admin"""
        self.navigate_to_main_app()
        self.find_and_click_created_survey(survey_title)
        self.submit_survey_filter()
        self.wait_for_success_message()
        self.click_okay_on_success()

    def complete_survey_flow(self, survey_data: dict, question_text: str):
        """Complete the entire survey creation and submission flow"""
        # Create the survey
        self.create_complete_survey(survey_data, question_text)
        
        # Submit the survey as admin
        self.submit_survey_as_admin(survey_data["title"])
        
        return True