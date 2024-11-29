Feature: Login feature

  Background:
    Given  i navigated to login page
    When   i validate the title

  @smoke69
  Scenario: Login with Valid Credentials
    Then   i enter valid credentials into respective textfield
    And    user should login successfully

  @smoke89
  Scenario: Login with inValid Credentials
    Then   i enter invalid credentials into respective textfield
    And    user should not  login successfully

  @smoke79
  Scenario: Login with only email Credential
    Then   i enter email credential into respective textfield
    And    user should not  login successfully

  @smoke99
  Scenario: Login with only password Credential
    Then   i enter password Credential into respective textfield
    And    user should not  login successfully