Feature: Add to cart functionality
  Background:
    Given i navigated to login page
    When i entered email  and password  into respective fields


  Scenario: search any product add to cart
    And  i entered product into search textfield
    And i clicked on add to cart btn
    Then successfully product should be added to cart should display

  Scenario: remove added  product from  cart
    And i clicked on  cart link
    And i clicked on remove btn
    Then then product  should be removed from cart should display