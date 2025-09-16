Feature: Add Event Image
  As a user
  I want to add images to an event
  So that I can share visual content and enhance the event experience

  Scenario Outline: Successful event image addition using valid image file
    Given <user_role> is logged in
    When I navigate to event details and add an image with valid data
    Then the Done button should be visible

    Examples:
      |   user_role    |
      |   citizen        |