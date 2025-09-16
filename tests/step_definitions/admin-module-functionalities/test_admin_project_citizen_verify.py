import pytest
import time
from pytest_bdd import given, scenarios, when, then, scenario, parsers
from pages.login_page import LoginPage
from pages.admin_project_page import AdminProjectPage
from pages.project_search_page import ProjectSearchPage
import json

@scenario('../../features/admin-features/admin_project_citizen_verify.feature', 'Admin creates project and citizen verifies it is visible')
def test_admin_create_project_citizen_verify():
    pass

@when(parsers.parse('I create a new project with name "{project_name}"'))
def when_create_project(page, project_name):
    admin_project_page = AdminProjectPage(page)
    
    # Navigate to projects section
    admin_project_page.navigate_to_projects()
    
    # Generate unique timestamp for project names (using today's date format)
    timestamp = "2025-09-16"
    unique_timestamp = str(int(time.time()))[-6:]  # Last 6 digits for uniqueness
    
    # Create project data with timestamp
    project_data = {
        "name_arabic": f"مشروع اختبار {timestamp}-{unique_timestamp}",
        "name_english": f"{project_name} {timestamp}-{unique_timestamp}",
        "description_arabic": "وصف مشروع اختبار إدارة",
        "description_english": "Admin test project description",
        "start_date": "16, Tuesday, September 16, 2025, Today",
        "partners": "Test Partners"
    }
    
    # Store project data for later verification
    page.add_init_script(f"window.testProjectData = {json.dumps(project_data)}")
    
    # Create the project
    admin_project_page.create_project(project_data)

@then('the project should be created successfully')
def then_project_created(page):
    # The success is handled in the create_project method
    # We're back on the Strategic Projects page
    page.wait_for_timeout(1000)

@when('I logout as admin and login as citizen')
def when_logout_admin_login_citizen(page, config):
    # Navigate to login page (logout)
    page.goto(config['app_login_page_url'])
    
    # Login as citizen
    login_page = LoginPage(page)
    login_page.login("citizen", config)

@when('I search for the created project')
def when_search_for_project(page):
    project_search_page = ProjectSearchPage(page)
    
    # Get the project data from the page context
    project_data = page.evaluate("window.testProjectData")
    project_name = project_data["name_english"]
    
    # Navigate to projects and search
    project_search_page.navigate_to_projects()
    project_search_page.search_for_project(project_name)

@then('I should find the project in search results with correct details')
def then_find_project_in_search(page):
    project_search_page = ProjectSearchPage(page)
    
    # Get the project data from the page context
    project_data = page.evaluate("window.testProjectData")
    project_name = project_data["name_english"]
    
    # Verify project appears in search results and details are correct
    project_search_page.verify_project_details(project_name)

@pytest.fixture(scope="session")
def config():
    with open("config.json", "r") as f:
        return json.load(f)