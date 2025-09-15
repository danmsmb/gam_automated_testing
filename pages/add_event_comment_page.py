import os
from playwright.sync_api import Page
from pages.base_page import BasePage

class AddEventCommentPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Main page elements
        self.search_textbox = page.get_by_role("textbox", name="Discover events near you....")
        self.first_event_image = page.get_by_role("img").first
        
        # Event details navigation
        self.view_details_button = page.get_by_role("button", name="View details...").first
        
        # Event details page elements
        self.back_button = page.get_by_role("button", name="Back")
        self.event_title = page.locator("[class*='CitizenEventDetailsScreen.EventName']")
        
        # Comment form elements
        self.comment_textbox = page.get_by_role("textbox", name="Share your opinion...")
        self.add_comment_button = page.get_by_text("Add Comment")
        self.submit_button = page.get_by_role("button", name="Add Comment")
        self.add_image_button = page.get_by_role("button", name="RatingCommentComponent.AddImage Add Image RatingCommentComponent.AddImage.Icon")
        
        # Rating elements (stars)
        self.rating_stars = page.locator("[role='img']").filter(has_text="")
        
        # Success confirmation
        self.success_dialog_ok_button = page.get_by_role("button", name="okay")
        
    

    def navigate_to_first_event(self):
        """Click on the first event card to expand details"""
        self.first_event_image.click()

    def click_view_details(self):
        """Click the view details button to go to event details page"""
        self.view_details_button.click()

    def fill_comment(self, comment_text: str):
        """Fill the comment text field"""
        self.comment_textbox.scroll_into_view_if_needed()
        self.comment_textbox.click()
        self.comment_textbox.fill(comment_text)
        # Give the form a moment to update
        self.page.wait_for_timeout(1000)

    def set_rating(self, rating: int):
        """Set rating by clicking on the appropriate star (1-5)"""
        if 1 <= rating <= 5:
            # Stars are indexed from 0, so rating-1
            star_index = rating - 1
            self.rating_stars.nth(star_index).click()

    def click_add_comment(self):
        """Click the add comment button to submit"""
        try:
            self.add_comment_button.click()
        except:
            # Try alternative selector if first one fails
            self.submit_button.click()

    def click_success_ok(self):
        """Click OK on the success dialog"""
        self.success_dialog_ok_button.click()

    def wait_for_success_dialog(self):
        """Wait for the success dialog to appear"""
        self.success_dialog_ok_button.wait_for(state="visible", timeout=10000)

    def add_event_comment(self, comment_data: dict):
        """Complete event comment addition with provided data"""
        self.navigate_to_first_event()
        self.click_view_details()
        
        # Add comment
        self.fill_comment(comment_data["comment_text"])
        self.click_add_comment()
        
        # Handle success dialog
        self.wait_for_success_dialog()
        self.click_success_ok()


    def is_comment_visible(self, comment_text: str):
        """Check if the comment is visible on the page"""
        return self.page.get_by_text(comment_text).is_visible()
