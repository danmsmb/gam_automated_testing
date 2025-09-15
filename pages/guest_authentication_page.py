import os
from playwright.sync_api import Page
from pages.base_page import BasePage

class GuestAuthenticationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Login page elements
        self.enter_as_guest_button = page.get_by_role("button", name="Enter as Guest")
        
        # Main page navigation elements
        self.notifications_nav = page.get_by_role("switch", name="NavItem.Notifications")
        self.home_nav = page.get_by_role("switch", name="NavItem.Home")
        
        # Event elements
        self.event_like_button = page.get_by_text("event_like_button").first
        
        # Authentication prompt dialog elements
 
        self.continue_as_guest_button = page.get_by_role("button", name="Continue as guest")
        self.sign_in_button = page.get_by_role("button", name="Sign In")
    
        
        # Login page elements
        self.username_input = page.get_by_role("textbox", name="Enter your username")
        self.password_input = page.get_by_role("textbox", name="Password", exact=True)
        self.login_button = page.get_by_role("button", name="Login", exact=True)

    def load_login_page(self, config):
        """Navigate to login page"""
        self.page.goto(config['app_login_page_url'])

    def click_enter_as_guest(self):
        """Click Enter as Guest button"""
        self.enter_as_guest_button.click()

    def click_notifications(self):
        """Click on notifications navigation"""
        self.notifications_nav.click()

    def click_event_like_button(self):
        """Click on the first event like button"""
        self.event_like_button.click()

    def click_continue_as_guest(self):
        """Click Continue as guest button in the dialog"""
        self.continue_as_guest_button.click()

    def click_sign_in_from_dialog(self):
        """Click Sign In button in the dialog"""
        self.sign_in_button.click()

    

    def is_on_login_page(self):
        """Check if we're on the login page"""
        return "login" in self.page.url

    def enter_as_guest_and_access_feature(self, feature_type: str):
        """Enter as guest and try to access a protected feature"""
        self.click_enter_as_guest()
        self.page.wait_for_timeout(2000)  # Wait for page to load
        
        if feature_type == "notifications":
            self.click_notifications()
        elif feature_type == "like_event":
            self.click_event_like_button()
        

    def verify_authentication_prompt_and_sign_in(self):
        """Verify the auth prompt is shown and click Sign In"""
        self.click_sign_in_from_dialog()
        self.page.wait_for_timeout(2000)  # Wait for navigation to login page
