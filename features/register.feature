Feature: Register Functionality

  Background:
    Given i navigated to register page
     Then i validated the page title


  Scenario: user should login
    Then i enter detail into name textfield
    When i clicked on submit button
    And user should login successfully


