Feature: Guest User Authentication Prompt
  As a guest user
  I want to be prompted to login when trying to access features that require authentication
  So that I know which features require an account

  Scenario Outline: Guest user accessing protected features prompts for login
    Given user enters as guest
    When I try to access <protected_feature>
    Then I can choose to sign in or continue as guest

    Examples:
      | protected_feature |
      | notifications     |
      | like_event        |
