Feature: Add Project Suggestion
  As a user
  I want to add a suggestion to an ongoing project
  So that I can contribute ideas for project improvement

  Scenario Outline: Successful project suggestion addition using valid data
    Given <user_role> is logged in
    When I navigate to an ongoing project and add a suggestion with valid data
    Then the suggestion should be submitted successfully

    Examples:
      |   user_role    |
      |   citizen        |
