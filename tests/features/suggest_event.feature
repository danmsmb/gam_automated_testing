Feature: Suggest Event
  As a user
  I want to suggest an event
  So that I people can register to the event

  Scenario Outline: Successful event suggestion using valid data
    Given <user_role> is logged in
    When I fill in the suggest event form with valid data
    Then the event should be submitted successfully

    Examples:
      |   user_role    |
      |   citizen        |

