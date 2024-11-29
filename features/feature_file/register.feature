Feature: Register Functionality

  Background:
    Given i navigated to register page
     Then i validated the page title

  @smoke1
  Scenario: user should login
    Then i enter detail into name textfield
    When i clicked on submit button
    And user should login successfully


  @smoke2
  Scenario: user should login without mandatory_fields
    Then i enter detail into  textfield
    When i clicked on submit button
    And user should login successfully

  @smoke3
  Scenario: user should login with only firstname
    Then i enter detail into firstname  textfield
    When i clicked on submit button
    And user should get proper error message should display