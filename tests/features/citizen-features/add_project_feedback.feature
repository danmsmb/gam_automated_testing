Feature: Add Project Feedback
  As a user
  I want to add feedback to a completed project
  So that I can share my experience and impact of the project

  Scenario Outline: Successful project feedback addition using valid data
    Given <user_role> is logged in
    When I navigate to a completed project and add feedback with valid data
    Then the feedback should be submitted successfully

    Examples:
      |   user_role    |
      |   citizen        |
