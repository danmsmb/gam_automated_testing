Feature: Citizen Project Filter by Status
  As a citizen
  I want to filter projects by their status
  So that I can find projects that match my interest level

  Scenario Outline: Filter projects by status and verify all results match the selected status
    Given <user_role> is logged in
    When I navigate to the projects section
    And I filter projects by "<status>" status
    Then I should see projects filtered by the selected status
    And all displayed projects should have "<status>" status labels
    And the "<status>" filter button should be active

    Examples:
      |   user_role    |   status    |
      |   citizen      |   planned   |
      |   citizen      |   ongoing   |
      |   citizen      |   completed |