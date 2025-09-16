Feature: Add Place
  As a user
  I want to add a place
  So that people can discover and visit the place

  Scenario Outline: Successful place addition using valid data
    Given <user_role> is logged in
    When I fill in the add place form with valid data
    Then the place should be submitted successfully

    Examples:
      |   user_role    |
      |   citizen        |
