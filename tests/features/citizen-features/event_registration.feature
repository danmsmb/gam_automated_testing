Feature: Event Registration
  As a citizen user
  I want to register for an event
  So that I can participate in the event

  Scenario Outline: Successful event registration with valid data
    Given <user_role> is logged in
    When I navigate to the first event details and register with valid data
    Then the Register Me button should no longer be visible


    Examples:
      |   user_role    |
      |   citizen        |