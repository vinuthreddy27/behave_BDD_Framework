Feature: gift functionality
  @fun
  Scenario: Send gift to an user
    Given  i nagigated to login page
    When  i enter valid credentials into respective textfield
    And  i clicked on gift cerficates
    And enter all the credentials into fields
    Then gift sent successfully message should display