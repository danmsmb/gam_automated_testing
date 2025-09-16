Feature: Admin Add Place
  As an admin user
  I want to add new places from the admin interface
  So that I can manage place suggestions and additions directly

  Scenario Outline: Admin successfully adds a new place
    Given <user_role> is logged in
    When I navigate to the Map section from admin interface
    And I click on Add New Place from admin map
    And I fill in the add place form with valid data
    Then the page URL should be "https://gamail.dev.internal.sirenanalytics.com/gamail_web/sideMenu"

    Examples:
      |   user_role    |
      |   admin        |