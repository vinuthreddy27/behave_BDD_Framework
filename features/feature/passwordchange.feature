Feature: password_change functionality

  Scenario: change current password
    Given  i nagigated to login page
    When  i enter valid credentials into respective textfield
    And i click on change password link
    And  do necessary changes
    Then password changed message should dispaly