Feature: Citizen Survey Submission
  As a citizen user
  I want to fill out and submit surveys
  So that I can provide feedback and verify submission status

  Scenario Outline: Successful survey submission and verification
    Given <user_role> is logged in
    When I navigate to the surveys section
    And I click on the first available survey
    And I fill out the survey with valid response
    And I submit the survey
    Then the survey should be submitted successfully
    When I try to access the same survey again
    Then I should see the already submitted message

    Examples:
      |   user_role    |
      |   citizen      |