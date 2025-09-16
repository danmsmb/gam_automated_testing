import os
from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.username_input = page.get_by_role("textbox", name="Enter your username")
        self.password_input = page.get_by_role("textbox", name="Password", exact=True)
        self.login_button = page.get_by_role("button", name="Login", exact=True)
        

        
        # Error message elements
        self.error_message = page.get_by_text("Invalid username or password")
        self.welcome_text = page.get_by_text("Welcome back")
        self.login_prompt_text = page.get_by_text("Please login to continue")
       

    def load(self, config):
            self.page.goto(config['app_login_page_url'])

    
    def fill_username(self, username: str):
        """Fill username field"""
        self.username_input.fill(username)
    
    def fill_password(self, password: str):
        """Fill password field"""
        self.password_input.fill(password)
    
    def click_login(self):
        """Click the login button"""
        self.login_button.click()

      # Login in to GAM by input username and password
    def login(self, user_role, config) -> None:
       self.page.wait_for_timeout(7000)
       if user_role == 'citizen':
          
            self.username_input.click()
            self.username_input.fill(config['citizen_user'])
            self.page.wait_for_timeout(2000)
            self.password_input.click()
            self.password_input.fill(config['citizen_password'])
            self.page.wait_for_timeout(2000)
            self.login_button.click()
       elif user_role == 'admin':
            self.username_input.click()
            self.username_input.fill(config['admin_user'])
            self.page.wait_for_timeout(2000)
            self.password_input.click()
            self.password_input.fill(config['admin_password'])
            self.page.wait_for_timeout(2000)
            self.login_button.click()
  
           

    def attempt_invalid_login(self, username: str, password: str):
        """Attempt login with invalid credentials"""
        self.page.wait_for_timeout(5000)
        self.fill_username(username)
        self.page.wait_for_timeout(2000)
        self.password_input.click()
        self.fill_password(password)
        self.page.wait_for_timeout(1000)
        
        self.click_login()
        self.page.wait_for_timeout(3000)  # Wait for error message to appear

    def is_error_message_visible(self):
        """Check if error message is visible"""
        return self.error_message.is_visible()

    def is_on_login_page(self):
        """Check if we're still on the login page"""
        return "login" in self.page.url and (self.welcome_text.is_visible() or self.login_prompt_text.is_visible())

    def get_error_message_text(self):
        """Get the error message text"""
        try:
            return self.error_message.text_content()
        except:
            return ""

   
