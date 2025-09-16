Feature: Admin Survey Filter Template Creation
  As an admin user
  I want to create survey filter templates
  So that I can target specific demographics for surveys

  Scenario Outline: Successful survey filter template creation
    Given <user_role> is logged in
    When I navigate to survey filter templates section
    And I click create new survey template
    And I fill the survey filter template with valid data
    And I submit the survey filter template
    Then the okay button should be visible

    Examples:
      |   user_role    |
      |   admin        |