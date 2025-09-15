Feature: Event Search Functionality
  As a citizen user
  I want to search for events on the homepage
  So that I can find specific events I'm interested in

  Scenario: Search for existing and non-existing events
    Given <user_role> is logged in
    When I search for an existing event "test-location"
    Then I should see the event in the search results
    When I search for a non-existing event "xyz123nonexistent"
    Then I should see the no events message

     Examples:
        |   user_role    |
        |   citizen        |

