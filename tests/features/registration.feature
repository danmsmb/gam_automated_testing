Feature: User Registration
  As a new user
  I want to register for an account
  So that I can access the application

  Scenario Outline: Successful user registration with valid data
    Given User is on the registration page
    When I fill in the registration form with the following details:
      | nationality              | <nationality>              |
      | national_personal_number | <national_personal_number> |
      | national_id_number       | <national_id_number>       |
      | username                 | <username>                 |
      | first_name               | <first_name>               |
      | last_name                | <last_name>                |
      | phone_number             | <phone_number>             |
      | email                    | <email>                    |
      | gender                   | <gender>                   |
      | location                 | <location>                 |
      | password                 | <password>                 |
      | confirm_password         | <confirm_password>         |
      | otp_code                 | <otp_code>                 |
    Then the registration should be completed successfully

    Examples:
      | nationality     | national_personal_number | national_id_number | username      | first_name | last_name | phone_number | email                | gender | location | password       | confirm_password | otp_code |
      | Jordanian       | auto_npn                 | auto_idn           | auto_username | Test       | User      | auto_phone   | testuser@example.com | Female | Basman   | StrongPass123! | StrongPass123!   | 123456  |
      | Non-Jordanian   | auto_npn                 | auto_idn           | auto_username | Test       | User      | auto_phone   | testuser@example.com | Male | Basman   | StrongPass123! | StrongPass123!   | 123456  |
