import os
from playwright.sync_api import Page
from tests.step_definitions.conftest import config
from pages.base_page import BasePage

class LanguageSwitchPage(BasePage):
    """Page object for language switching functionality"""
    
    def __init__(self, page: Page):
        super().__init__(page)
        
        # Language switch button
        self.language_button = page.get_by_role("button", name="language_icon")
        
        # Login page selectors (English)
        self.welcome_text_en = page.get_by_text("Welcome back")
        self.login_subtitle_en = page.get_by_text("Please login to continue")
        self.username_label_en = page.get_by_text("Username")
        self.password_label_en = page.get_by_text("Password", exact=True)
        self.login_button_en = page.get_by_role("button", name="Login")
        self.username_input_en = page.get_by_role("textbox", name="Enter your username")
        self.password_input_en = page.get_by_role("textbox", name="Password")
        
        # Login page selectors (Arabic)
        self.welcome_text_ar = page.get_by_text("مرحبًا بعودتك")
        self.login_subtitle_ar = page.get_by_text("يرجى تسجيل الدخول للمتابعة")
        self.username_label_ar = page.get_by_text("اسم المستخدم")
        self.password_label_ar = page.get_by_text("كلمة المرور" , exact=True)
        self.login_button_ar = page.get_by_role("button", name="تسجيل الدخول")
        self.username_input_ar = page.get_by_role("textbox", name="ادخل اسم المستخدم")
        self.password_input_ar = page.get_by_role("textbox", name="كلمة المرور")
        
        # Main page selectors (English)
        self.search_box_en = page.get_by_role("textbox", name="Discover events near you")
        self.upcoming_button_en = page.get_by_role("button", name="Upcoming")
        self.today_button_en = page.get_by_role("button", name="Today")
        self.tomorrow_button_en = page.get_by_role("button", name="Tomorrow")
        self.weekend_button_en = page.get_by_role("button", name="Weekend")
        self.show_map_button_en = page.get_by_role("button", name="Show Map")
        self.social_category_en = page.get_by_role("button", name="Social")
        
        # Main page selectors (Arabic)
        self.search_box_ar = page.get_by_role("textbox", name="اكتشف الفعاليات بجانبك")
        self.upcoming_button_ar = page.get_by_role("button", name="القادم")
        self.today_button_ar = page.get_by_role("button", name="اليوم")
        self.tomorrow_button_ar = page.get_by_role("button", name="غداً")
        self.weekend_button_ar = page.get_by_role("button", name="نهاية الأسبوع")
        self.show_map_button_ar = page.get_by_role("button", name="عرض الخريطة")
        self.social_category_ar = page.get_by_role("button", name="اجتماعية")
        
    def navigate_to_login_page(self):
        """Navigate to the login page"""
        self.page.goto("https://gamail.dev.internal.sirenanalytics.com/gamail_web/login")
        self.page.wait_for_timeout(3000)
        
    def click_language_switch(self):
        """Click the language switch button"""
        self.language_button.click()
        self.page.wait_for_timeout(2000)
        
    def login_as_citizen(self, username: str, password: str):
        """Login as a citizen user (works for both languages)"""
        # Try English inputs first
        self.page.wait_for_timeout(7000)
        if self.username_input_en.is_visible():
            self.username_input_en.click()
            self.username_input_en.fill(username)
            self.page.wait_for_timeout(1000)
            self.password_input_en.click()
            self.password_input_en.fill(password)
            self.page.wait_for_timeout(1000)
            self.login_button_en.click()
        # Try Arabic inputs if English not visible
        elif self.username_input_ar.is_visible():
            
            self.username_input_ar.click()
            self.username_input_ar.fill(username)
            self.page.wait_for_timeout(1000)
            self.password_input_ar.click()
            self.password_input_ar.fill(password)
            self.page.wait_for_timeout(1000)
            self.login_button_ar.click()
        
        self.page.wait_for_timeout(3000)
        
    def verify_login_page_english(self) -> bool:
        """Verify that the login page is displayed in English"""
        return (self.welcome_text_en.is_visible() and 
                self.login_subtitle_en.is_visible() and
                self.username_label_en.is_visible() and
                self.password_label_en.is_visible())
                
    def verify_login_page_arabic(self) -> bool:
        """Verify that the login page is displayed in Arabic"""
        return (self.welcome_text_ar.is_visible() and 
                self.login_subtitle_ar.is_visible() and
                self.username_label_ar.is_visible() and
                self.password_label_ar.is_visible())
                
    def verify_main_page_english(self) -> bool:
        """Verify that the main page is displayed in English"""
        return (self.upcoming_button_en.is_visible() and 
                self.today_button_en.is_visible() and
                self.tomorrow_button_en.is_visible() and
                self.social_category_en.is_visible())
                
    def verify_main_page_arabic(self) -> bool:
        """Verify that the main page is displayed in Arabic"""
        return (self.upcoming_button_ar.is_visible() and 
                self.today_button_ar.is_visible() and
                self.tomorrow_button_ar.is_visible() and
                self.social_category_ar.is_visible())
    
    def get_current_language_on_login_page(self) -> str:
        """Get the current language on login page"""
        if self.verify_login_page_english():
            return "English"
        elif self.verify_login_page_arabic():
            return "Arabic"
        else:
            return "Unknown"
            
    def get_current_language_on_main_page(self) -> str:
        """Get the current language on main page"""
        if self.verify_main_page_english():
            return "English"
        elif self.verify_main_page_arabic():
            return "Arabic"
        else:
            return "Unknown"