Feature: Survey Management
  As an admin user
  I want to create and manage surveys
  So that I can collect feedback from users

  Scenario Outline: Complete survey creation and submission flow
    Given admin is on Surveyio
    When I create a new survey with a long text question
    And I save, publish, and enable the survey
    And I navigate to the main app and submit the survey filter
    Then I should see a success message and be able to confirm it

    Examples:
      |   user_role    |
      |   admin        |