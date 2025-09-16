Feature: login

  Scenario Outline: login
    Given <user_role> is logged in

    Examples:
      |   user_role    |
      |   citizen        |

