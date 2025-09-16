from playwright.sync_api import Page, expect
from pages.suggest_event_page import SuggestEventPage


class AdminCreateEventPage(SuggestEventPage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Admin-specific locators
        self.create_event_menu = page.get_by_text("Create Event")
        self.create_event_button = page.get_by_role("button", name="Create Event")
        self.events_list_header = page.get_by_text("Events", exact=True)
        
        # Event management locators
        self.manage_events_menu = page.get_by_text("Manage Events")
        self.dashboard_menu = page.get_by_text("Dashboard")
        self.view_details_button = page.get_by_role("button", name="View Details")
        self.edit_button = page.get_by_role("button", name="Edit")
        self.set_button = page.get_by_role("button", name="Set")
        self.dashboard_search_box = page.get_by_role("textbox", name="Search")
        self.view_details_button_event_card = page.get_by_role("button", name="View details...")
        
    def navigate_to_create_event(self):
        """Navigate to create event from admin panel"""
        self.create_event_menu.click()
        self.page.wait_for_timeout(2000)
        
    def create_admin_event(self, event_data: dict):
        """Create a new event using admin interface (reuses suggest event form)"""
        # Convert admin event data format to suggest event format
        suggest_event_data = {
            "event_name_ar": event_data["name_arabic"],
            "event_name_en": event_data["name_english"],
            "start_date": event_data["start_date"],
            "end_date": event_data["end_date"],
            "event_description_ar": event_data["description_arabic"],
            "event_description_en": event_data["description_english"]
        }
        
        # Fill the form using the inherited method from SuggestEventPage
        self._fill_event_form(suggest_event_data, event_data)
        
        # Click Create Event button (different from suggest event)
        self.create_event_button.click()
        self.page.wait_for_timeout(3000)
        
    def _fill_event_form(self, suggest_data: dict, admin_data: dict):
        """Fill the event form (reused logic from suggest event page)"""
        # Fill event names
               # Set location
        self.page.wait_for_timeout(1000)
        self.location_list.click()
        self.page.wait_for_timeout(1000)
        self.location_option.click()
        self.page.wait_for_timeout(1000)
        self.suggested_event_name_ar_input.click()
        self.suggested_event_name_ar_input.fill(suggest_data["event_name_ar"])
        self.page.wait_for_timeout(2000)
        self.suggested_event_name_en_input.click()
        self.suggested_event_name_en_input.fill(suggest_data["event_name_en"])
        self.page.wait_for_timeout(1000)
        
        # Set dates
        self.start_date_input.click()
        self.page.get_by_role("button", name=suggest_data["start_date"]).click()
        self.date_ok_button.click()
        self.date_ok_button.click()
        self.page.wait_for_timeout(1000)
        self.end_date_input.click()
        self.page.get_by_role("button", name=suggest_data["end_date"]).click()
        self.date_ok_button.click()
        self.date_ok_button.click()
        self.page.wait_for_timeout(1000)

 
        
        # Set category
        self.page.wait_for_timeout(1000)
        self.event_category_list.scroll_into_view_if_needed()
        self.event_category_list.click()
        self.page.get_by_role("button", name=admin_data["category"]).click()
        self.done_button.click()
        
        # Set accessibility
        self.page.wait_for_timeout(1000)
     
        self.event_accessibility_list.click()
        self.page.get_by_role("button", name=admin_data["accessibility"]).click()
        self.done_button.click()
        
        # Fill descriptions
        self.page.wait_for_timeout(2000)
      
        self.event_description_input_ar.click()
        self.event_description_input_ar.fill(suggest_data["event_description_ar"])
        self.page.wait_for_timeout(3000)

        self.event_description_input_en.click()
        self.event_description_input_en.fill(suggest_data["event_description_en"])
        self.page.wait_for_timeout(1000)
        
    def verify_event_created(self):
        """Verify the event was created successfully by checking if we're back to events list"""
        expect(self.events_list_header).to_be_visible()
        
    def logout_admin(self):
        """Logout from admin panel"""
        self.page.goto("https://gamail.dev.internal.sirenanalytics.com/gamail_web/login")
        
    def navigate_to_manage_events(self):
        """Navigate to manage events from admin panel"""
        self.manage_events_menu.click()
        self.page.wait_for_timeout(3000)
        
    def edit_first_event_name(self, new_name: str):
        """Edit the first event in the list and change its English name"""
        # Click View Details on the first event
        self.view_details_button.first.click()
        self.page.wait_for_timeout(2000)
        
        # Click Edit button
        self.edit_button.click()
        self.page.wait_for_timeout(2000)
        
        # Find and update the English event name field
        
        self.suggested_event_name_en_input.click()
        self.page.keyboard.press('Control+a')
        self.suggested_event_name_en_input.fill(new_name)
        self.page.wait_for_timeout(1000)
        
        # Save changes
        self.set_button.click()
        self.page.wait_for_timeout(3000)
        
    def navigate_to_dashboard(self):
        """Navigate to dashboard from admin panel"""
        self.dashboard_menu.click()
        self.page.wait_for_timeout(3000)
        
    def search_for_event(self, search_term: str):
        """Search for an event in the dashboard"""
        self.dashboard_search_box.click()
        self.dashboard_search_box.fill(search_term)
        self.page.wait_for_timeout(3000)
        
    def verify_event_found_in_search(self, event_name: str):
        """Verify that the event appears in search results"""
        self.view_details_button_event_card.first.click()
        self.page.wait_for_timeout(2000)
        event_card = self.page.get_by_text(event_name)
        expect(event_card).to_be_visible()
        
    def verify_event_updated_successfully(self):
        """Verify the event was updated successfully by checking if we're back to manage events"""
        expect(self.events_list_header).to_be_visible()