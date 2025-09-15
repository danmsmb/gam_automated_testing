Feature: Logout

  Scenario Outline: Logout
    Given <user_role> is logged in
    When User clicks on Logout
    Then User should be logged out

    Examples:
      |   user_role    |
      |   citizen        |

