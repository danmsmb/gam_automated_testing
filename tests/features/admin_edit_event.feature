Feature: Admin Edit Event and Verify Changes
  As an admin
  I want to edit existing events
  So that I can update event information and verify changes are reflected in the dashboard

  Scenario: Admin edits event name and verifies it in dashboard search
    Given I am logged in as admin
    When I navigate to manage events
    And I edit an existing event name to "Admin Edited Event Test 2025"
    Then the event should be updated successfully
    When I navigate to dashboard
    And I search for "Admin Edited Event Test 2025"
    Then I should find the updated event in search results