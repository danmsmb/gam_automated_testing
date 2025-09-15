import os
from playwright.sync_api import Page
from tests.step_definitions.conftest import config
from pages.base_page import BasePage
import re, time
from playwright.sync_api import expect

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.jordanian_radio = page.get_by_role("radio", name="Jordanian", exact=True)
        self.non_jordanian_radio = page.get_by_role("radio", name="Non-Jordanian")
        
        # Initialize locators
        self.national_personal_number = page.get_by_role("textbox", name="National / Personal Number")
        self.national_id_number = page.get_by_role("textbox", name="ID Number * ID Number")

          # --- Non-Jordanian fields ---
        self.nj_personal =  page.get_by_role("textbox", name="Personal Number * Personal")
        self.nj_document = page.get_by_role("textbox", name="Document Number * Document")

        self.date_of_birth = page.get_by_role("textbox", name="Date Of Birth")
        self.username = page.get_by_role("textbox", name="Username * Username")
        self.first_name = page.get_by_role("textbox", name="First Name * First Name")
        self.last_name = page.get_by_role("textbox", name="Last Name * Last Name")
        self.phone_number =  page.get_by_role("textbox", name="Phone Number e.g : 07XXXXXXXX")
        self.email = page.get_by_role("textbox", name="Email * Email")
        self.password = page.get_by_role("textbox", name="Password Password")
        self.confirm_password = page.get_by_role("textbox", name="Confirm Password Confirm")
        self.gender_button =   page.get_by_role("button", name="Gender * Gender")
        self.location_button = page.get_by_role("button", name="Location * Enter location...")
        self.terms_checkbox = page.get_by_role("checkbox", name="Accept Terms and Conditions")
        self.register_button = page.get_by_role("button", name="Register now")

        #self.otp_field = self.page.locator("#one-time-code")

        # Date picker elements
        self.select_year_button = page.get_by_role("button", name="Select year")
        self.year_2004_button = page.get_by_role("button", name="2004")
        self.ok_button = page.get_by_role("button", name="OK")

        self.okay_btn =  page.get_by_role("button", name="okay")
        
        # Popup menu elements
        self.popup_menu = page.get_by_label("Popup menu")

    def load(self, config):
            self.page.goto(config['app_registration_page_url'])

    
    def select_nationality(self, nationality: str):
        nationality = (nationality or "").strip().lower()
        if nationality in ("jordanian", "jo", "jordan"):
            self.jordanian_radio.click()
        elif nationality in ("non-jordanian", "non jordanian", "non_jo"):
            self.non_jordanian_radio.click()
        else:
            raise ValueError(f"Unknown nationality: {nationality}")
    
    def fill_national_personal_number(self, number: str):
        """Fill national/personal number field"""
        self.national_personal_number.click()
        self.national_personal_number.fill(number)
        
    def fill_national_id_number(self, number: str):
        """Fill national ID number field"""
        self.national_id_number.click()
        self.national_id_number.fill(number)
    
    def select_date_of_birth(self):
        self.date_of_birth.click()
    
    # Wait and interact safely
        self.select_year_button.wait_for(state="visible", timeout=5000)
        self.select_year_button.click()
    
        self.year_2004_button.wait_for(state="visible", timeout=5000)
        self.year_2004_button.click()
    
        self.ok_button.wait_for(state="visible", timeout=5000)
        self.ok_button.click()

        self.page.wait_for_timeout(1000)
    

    
    def fill_username(self, username: str):
        """Fill username field"""
        self.username.scroll_into_view_if_needed()
        self.username.click()
        self.username.fill(username)
        self.page.wait_for_timeout(1000)
    

    def fill_first_name(self, first_name: str):
        """Fill first name field"""
        self.first_name.scroll_into_view_if_needed()
        self.first_name.click()
        self.first_name.fill(first_name)
        self.page.wait_for_timeout(1000)
    

    def fill_last_name(self, last_name: str):
        """Fill last name field"""
        self.last_name.scroll_into_view_if_needed()
        self.last_name.click()
        self.last_name.fill(last_name)
        self.page.wait_for_timeout(1000)
    

    def fill_phone_number(self, phone: str):
        """Fill phone number field"""
        self.phone_number.scroll_into_view_if_needed()
        self.phone_number.click()
        self.phone_number.fill(phone)
        self.page.wait_for_timeout(1000)
    

    def fill_email(self, email: str):
        """Fill email field"""
        self.email.scroll_into_view_if_needed()
        self.email.click()
        self.email.fill(email)
        self.page.wait_for_timeout(1000)
    

    def select_gender(self, gender: str):
        """Select gender from dropdown"""
        self.gender_button.click()
        self.popup_menu.get_by_text(gender, exact= True).click()
        self.page.wait_for_timeout(1000)
    
    
    def select_location(self, location: str):
        """Select location from dropdown"""
        self.location_button.click()
        self.popup_menu.get_by_text(location).click()
        self.page.wait_for_timeout(1000)
    
    def fill_password(self, password: str):
        """Fill password field"""
        self.password.fill(password)
        self.page.wait_for_timeout(2000)  # Increased timeout for password field
    
    def fill_confirm_password(self, password: str):
        """Fill confirm password field"""
        self.confirm_password.fill(password)
        self.page.wait_for_timeout(1000)
    
    
    def accept_terms(self):
        """Check terms and conditions checkbox"""
        self.terms_checkbox.scroll_into_view_if_needed()
        self.terms_checkbox.click()
    
    def click_register(self):
        """Click register button"""
        self.register_button.click()
        self.page.wait_for_timeout(3000)
    

    # def fill_otp_code(self, otp: str):
    #     try:
    #         print("📍 Clicking semantic node 9 to trigger OTP input...")

    #     # ✅ Step 1: Click known working node
    #         self.page.locator("[id^='flt-semantic-node-']").nth(9).click(force=True)
    #         self.page.wait_for_timeout(300)

    #     # ✅ Step 2: Wait for the OTP input to be injected
           
    #         for _ in range(10):
    #             if self.otp_field.count() > 0:
    #                 print("🎯 OTP input appeared.")
    #                 break
    #             self.page.wait_for_timeout(100)
    #         else:
    #             raise Exception("❌ OTP input not found in DOM after clicking node 9")

    #     # ✅ Step 3: Inject OTP value with JS
    #         self.page.evaluate(f"""
    #         () => {{
    #             const input = document.querySelector('#one-time-code');
    #             if (input) {{
    #                 input.value = '{otp}';
    #                 input.dispatchEvent(new Event('input', {{ bubbles: true }}));
    #                 input.dispatchEvent(new Event('change', {{ bubbles: true }}));
    #             }}
    #         }}
    #     """)

    #         print("✅ OTP code injected via JS.")
    #         self.page.wait_for_timeout(500)

    #     except Exception as e:
    #         print("❌ OTP entry failed:", e)
    #         raise


    def registration(self, user_data: dict):
        """Complete user registration with provided data"""
        self.select_nationality(user_data.get("nationality", "Jordanian"))

        
        self.page.wait_for_timeout(2000)
        if (user_data.get("nationality","Jordanian")).lower().startswith("non"):
            # Non-Jordanian fields
            self.nj_personal.fill(user_data["national_personal_number"])   # "Personal Number"
            self.nj_document.fill(user_data["national_id_number"])  
            self.page.wait_for_timeout(1000)
            if(self.okay_btn.is_visible()):
                self.okay_btn.click()      # "Document Number"
            if(self.okay_btn.is_visible()):
                self.okay_btn.click()      # "Document Number"
            
        else:
            self.fill_national_personal_number(user_data["national_personal_number"])
            self.fill_national_id_number(user_data["national_id_number"])  
            self.page.wait_for_timeout(1000)          # "ID Number"
      
        self.select_date_of_birth()
        self.page.wait_for_timeout(1000)
        if(self.okay_btn.is_visible()):
            self.okay_btn.click()
        self.fill_username(user_data["username"])
        self.page.wait_for_timeout(1000)
        if(self.okay_btn.is_visible()):
            self.okay_btn.click()
        self.fill_first_name(user_data["first_name"])
        self.page.wait_for_timeout(1000)
        if(self.okay_btn.is_visible()):
            self.okay_btn.click()
        self.fill_last_name(user_data["last_name"])
        self.page.wait_for_timeout(1000)
        if(self.okay_btn.is_visible()):
            self.okay_btn.click()
        self.page.wait_for_timeout(1000)
        self.fill_phone_number(user_data["phone_number"])
        self.fill_email(user_data["email"])
        self.select_gender(user_data["gender"])
        self.select_location(user_data["location"])
        self.fill_password(user_data["password"])
        self.page.wait_for_timeout(1000)
        self.fill_confirm_password(user_data["confirm_password"])
        self.accept_terms()
        self.click_register()
        #self.fill_otp_code(user_data["otp_code"])
