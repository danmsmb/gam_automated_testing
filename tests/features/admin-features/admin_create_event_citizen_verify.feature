Feature: Admin Create Event and Citizen Verification
  As an admin
  I want to create events
  So that citizens can see and interact with them

  Scenario: Admin creates event and citizen verifies it is visible
    Given <user_role> is logged in
    When I create a new event with name "Admin Test Event"
    Then the event should be created successfully
    When I logout as admin and login as citizen
    And I search for the created event
    Then I should find the event in search results with correct details
    When I register for the created event
    Then the registration should be successful

      Examples:
      | user_role |
      | admin     |