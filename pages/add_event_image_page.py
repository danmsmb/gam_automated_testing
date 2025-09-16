import os
from playwright.sync_api import Page
from pages.base_page import BasePage

class AddEventImagePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Main page elements
        self.search_textbox = page.get_by_role("textbox", name="Discover events near you....")
        
        
        # Event details navigation
        self.view_details_button = page.get_by_role("button", name="View details...").first
        
        # Event details page elements
        self.back_button = page.get_by_role("button", name="Back")
        self.event_title = page.get_by_text("Admin Test Event")
        
        # Image upload elements
        self.add_image_button = page.get_by_text("Add Image")
        self.choose_images_button = page.get_by_role("button", name="Choose Images")
        self.add_images_button = page.get_by_role("button", name="Add Images")
        self.done_button = page.get_by_role("button", name="Done")
        
    

    def click_view_details(self):
        """Click the view details button to go to event details page"""
        self.view_details_button.click()

    def click_add_image(self):
        """Click the add image button to start image upload process"""
        self.add_image_button.click()

    def click_choose_images(self):
        """Click the choose images button to open file dialog"""
        self.choose_images_button.click()

    def upload_image(self, image_path: str):
        """Upload an image file using the file chooser"""
        # Get absolute path
        absolute_path = os.path.abspath(image_path)
        
        # Click choose images to open file dialog
        self.click_choose_images()
        
        # Handle file upload (this will be handled by the test framework)
        # The actual file selection is done via file_upload tool in tests
        
    def click_add_images(self):
        """Click the add images button to submit the upload"""
        self.add_images_button.click()

    def click_done(self):
        """Click the Done button to complete the image addition process"""
        self.done_button.click()

    def is_done_button_visible(self):
        """Check if Done button is visible"""
        return self.done_button.is_visible()

    def wait_for_done_button(self):
        """Wait for the Done button to appear"""
        self.done_button.wait_for(state="visible", timeout=15000)

    def add_event_image(self, image_data: dict):
        """Complete event image addition with provided data"""
        self.page.wait_for_timeout(5000)
        self.click_view_details()
        self.page.wait_for_timeout(3000)
        
        # Add image
        self.click_add_image()
        self.page.wait_for_timeout(2000)
        
        # Note: File upload is handled separately in tests
        # This method assumes the file has been uploaded via file_upload tool
        
        # Click add images to submit
        self.click_add_images()
        self.page.wait_for_timeout(3000)
        
        # Verify done button appears
        self.wait_for_done_button()
        
        # Click done to complete
        self.click_done()

    def is_image_gallery_visible(self):
        """Check if photo gallery section is visible"""
        return self.photo_gallery.is_visible()