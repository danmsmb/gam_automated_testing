Feature: Add Event Comment
  As a user
  I want to add a comment to an event
  So that I can share my thoughts and feedback about the event

  Scenario Outline: Successful event comment addition using valid data
    Given <user_role> is logged in
    When I navigate to event details and add a comment with valid data
    Then the comment should be submitted successfully

    Examples:
      |   user_role    |
      |   citizen        |
