from playwright.sync_api import Page, expect


class ProjectSearchPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.get_by_role("textbox", name="Search Projects")
        
    def navigate_to_projects(self):
        """Navigate to the projects section"""
        projects_nav = self.page.get_by_role("switch", name="NavItem.Projects")
        projects_nav.click()
        self.page.wait_for_timeout(2000)  # Wait for page to load
        
    def search_for_project(self, search_term: str):
        """Search for a project using the search box"""
        self.search_input.click()
        self.search_input.fill(search_term)
        # Wait for search results to load
        self.page.wait_for_timeout(2000)
        
        
    def verify_project_details(self, project_name: str):
        """Verify project details by clicking View details and checking the project name"""
        # Click on the View details button for the first project
        view_details_button = self.page.get_by_role("button", name="View details...").first
        view_details_button.click()
        self.page.wait_for_timeout(2000)
        
        # Verify the project name appears on the details page
        project_title = self.page.get_by_text(project_name, exact=True)
        expect(project_title).to_be_visible()
        
        # Go back to the projects list
        back_button = self.page.get_by_role("button", name="Back")
        back_button.click()
        self.page.wait_for_timeout(2000)
        self.page.reload()
        self.page.wait_for_timeout(2000)
        self.navigate_to_projects()
        
    def verify_no_projects_message(self):
        """Verify that the 'no projects found' message is displayed"""
        no_projects_message = self.page.get_by_text("No projects found")
        expect(no_projects_message).to_be_visible()
        
    def verify_search_box_contains_text(self, text: str):
        """Verify that the search box contains the specified text"""
        expect(self.search_input).to_have_value(text)
