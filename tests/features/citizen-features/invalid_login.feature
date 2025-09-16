Feature: Invalid Login Credentials
  As a user
  I want to see an error message when I enter invalid credentials
  So that I know my login attempt failed and can try again

  Scenario Outline: Login with invalid credentials shows error message
    Given user is on the login page
    When I attempt to login with <username> and <invalid_password>
    Then I should see an error message
    And I should remain on the login page

    Examples:
      | username | invalid_password |
      | tia      | WrongPassword123 |
