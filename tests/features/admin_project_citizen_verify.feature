Feature: Admin Project Creation and Citizen Verification
  As an admin
  I want to create projects
  So that citizens can see and interact with them

  Scenario Outline: Admin creates project and citizen verifies it is visible
    Given <user_role> is logged in
    When I create a new project with name "Admin Test Project"
    Then the project should be created successfully
    When I logout as admin and login as citizen
    And I search for the created project
    Then I should find the project in search results with correct details

    Examples:
      | user_role |
      | admin     |