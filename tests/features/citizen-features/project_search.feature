Feature: Project Search Functionality
  As a citizen user
  I want to search for projects on the projects page
  So that I can find specific projects I'm interested in

  Scenario: Search for existing and non-existing projects
    Given <user_role> is logged in
    And I am on the projects page
    When I search for an existing project "dana-test"
    Then I should be able to view the project "dana-test" details
    When I search for a non-existing project "nonexistentproject12345"
    Then I should see the no projects message

     Examples:
        |   user_role    |
        |   citizen        |
