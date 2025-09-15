import os
from playwright.sync_api import Page
from pages.base_page import BasePage

class ChangePasswordPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Login page elements
        self.change_password_button = page.get_by_role("button", name="Change Password")
        
        # Change password page elements
        self.back_button = page.get_by_role("button", name="Back")
        self.page_heading = page.get_by_role("heading", name="Change Password")
        
        # Form elements
        self.username_input = page.get_by_role("textbox", name="Enter your username")
        self.request_otp_button = page.get_by_role("button", name="Request OTP")
        
        # Step 2 form elements (after OTP request)
        self.new_password_input = page.get_by_role("textbox", name="Enter New Password...")
        self.otp_code_input = page.get_by_role("textbox", name="OTP Code")
        self.change_password_submit_button = page.get_by_role("button", name="Change Password")
        self.resend_otp_button = page.get_by_role("button", name="Resend OTP")
        
        # Success confirmation
        self.success_dialog_ok_button = page.get_by_role("button", name="okay")
      
        
        # Login page elements (after successful change)
        self.login_username_input = page.get_by_role("textbox", name="Enter your username")
        self.login_password_input = page.get_by_role("textbox", name="Password", exact=True)
        self.login_button = page.get_by_role("button", name="Login", exact=True)

    def load_login_page(self, config):
        """Navigate to login page"""
        self.page.goto(config['app_login_page_url'])

    def click_change_password_from_login(self):
        """Click Change Password button from login page"""
        self.change_password_button.click()

    def fill_username(self, username: str):
        """Fill username field"""
        self.username_input.scroll_into_view_if_needed()
        self.username_input.click()
        self.username_input.fill(username)

    def click_request_otp(self):
        """Click Request OTP button"""
        self.request_otp_button.click()

    def fill_new_password(self, new_password: str):
        """Fill new password field"""
        self.new_password_input.scroll_into_view_if_needed()
        self.new_password_input.click()
        self.new_password_input.fill(new_password)

    def fill_otp_code(self, otp_code: str):
        """Fill OTP code field"""
        self.otp_code_input.scroll_into_view_if_needed()
        self.otp_code_input.click()
        self.otp_code_input.fill(otp_code)

    def click_change_password_submit(self):
        """Click Change Password submit button"""
        self.change_password_submit_button.click()

    def click_resend_otp(self):
        """Click Resend OTP button"""
        self.resend_otp_button.click()

    def click_success_ok(self):
        """Click OK on the success dialog"""
        self.success_dialog_ok_button.click()


    def wait_for_otp_form(self):
        """Wait for OTP form elements to appear after requesting OTP"""
        self.new_password_input.wait_for(state="visible", timeout=10000)
        self.otp_code_input.wait_for(state="visible", timeout=10000)

    def change_password_complete_flow(self, password_data: dict):
        """Complete change password flow with provided data"""
        # Step 1: Navigate to change password page and enter username
        self.click_change_password_from_login()
        self.page.wait_for_timeout(2000)  # Wait for page to load
        
        # Fill username and request OTP
        self.fill_username(password_data["username"])
        self.click_request_otp()
        
        # Wait for OTP form to appear
        self.wait_for_otp_form()
        self.page.wait_for_timeout(2000)  # Wait for form to be ready
        
        # Step 2: Fill new password and OTP, then submit
        self.fill_new_password(password_data["new_password"])
        self.fill_otp_code(password_data["otp_code"])
        self.click_change_password_submit()
        
        self.click_success_ok()


    def is_on_login_page(self):
        """Check if we're back on the login page"""
        return "login" in self.page.url

    def verify_login_with_new_password(self, username: str, new_password: str):
        """Verify login works with the new password"""
        self.page.wait_for_timeout(2000)  # Wait for login page to be ready
        self.login_username_input.fill(username)
        self.page.wait_for_timeout(1000)
        self.login_password_input.click()
        self.login_password_input.fill(new_password)
        self.login_button.click()
        self.page.wait_for_timeout(3000)  # Wait for login attempt
