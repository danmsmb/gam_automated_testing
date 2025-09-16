Feature: Change Password
  As a user
  I want to change my password
  So that I can update my account security

  Scenario Outline: Successful password change using valid data
    Given user is on the change password page
    When I request OTP for <username> and change password with valid data
    Then the password should be changed successfully

    Examples:
      | username               |
      | dana_change_password   |
