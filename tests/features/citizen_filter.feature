Feature: Citizen Event Filter by Accessibility
  As a citizen
  I want to filter events by accessibility features
  So that I can find events that meet my accessibility needs

  Scenario Outline: Filter events by wheelchair accessibility and verify results
    Given <user_role> is logged in
    When I open the filter dialog and select wheelchair accessibility
    And I apply the filters
    Then I should see filtered events
    When I view details of multiple events
    Then all events should show wheelchair accessibility

    Examples:
      |   user_role    |
      |   citizen      |