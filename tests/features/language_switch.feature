Feature: Language Switch Functionality
  As a user
  I want to switch the application language
  So that I can use the application in my preferred language

  Scenario Outline: Successful language switch from English to Arabic and back
    Given I am on the login page in English
    When I click the language switch button
    Then the page should be displayed in Arabic
    Given user logs in
    When I click the language switch button on main page
    Then the main page should be displayed in English
