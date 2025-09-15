import pytest
import allure
from pytest_bdd import given, scenarios, when, then, parsers, scenario
from pages.login_page import LoginPage
from pages.project_search_page import ProjectSearchPage
import json


@allure.title("Project search functionality validation")
@allure.description("""
Test Steps:
1. Navigate to projects page
2. Search for an existing project by name/keyword
3. Verify project appears in search results
4. Search for a non-existing project
5. Verify "no projects found" message is displayed

This test validates the project search functionality for both existing and non-existing projects.
""")
@allure.severity(allure.severity_level.CRITICAL)
@scenario('../features/project_search.feature', 'Search for existing and non-existing projects')
def test_project_search():
    pass


@given('I am on the projects page')
def given_on_projects_page(page):
    search_page = ProjectSearchPage(page)
    search_page.navigate_to_projects()


@when(parsers.parse('I search for an existing project "{search_term}"'))
def when_search_existing_project(page, search_term):
    search_page = ProjectSearchPage(page)
    search_page.search_for_project(search_term)


@then(parsers.parse('I should be able to view the project "{project_name}" details'))
def then_view_project_details(page, project_name):
    search_page = ProjectSearchPage(page)
    search_page.verify_project_details(project_name)


@when(parsers.parse('I search for a non-existing project "{search_term}"'))
def when_search_non_existing_project(page, search_term):
    search_page = ProjectSearchPage(page)
    search_page.search_for_project(search_term)


@then('I should see the no projects message')
def then_see_no_projects_message(page):
    search_page = ProjectSearchPage(page)
    search_page.verify_no_projects_message()


@pytest.fixture(scope="session")
def config():
    with open("config.json", "r") as f:
        return json.load(f)
