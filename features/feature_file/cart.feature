Feature: Add to cart functionality

  @init69
  Scenario: search any product add to cart
    Given i navigated to login page
    When i entered email  and password  into respective fields
    And  i entered product into search textfield
    And i clicked on add to cart btn
    Then successfully product should be added to cart should display
