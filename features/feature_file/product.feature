Feature: product search functionality

  @skip
  Scenario Outline: Search for valid product
    Given i navigated to homepage
    Then i login with valid credentials
    And i entered <products> into searchtextfield
    Then product should display
    Examples:
      | products  |
      |Apple Cinema 30|
      |MacBook      |
      |iphone       |
      |iphone 15pro|
