Feature: Review Functionality

Background:
    Given i navigated to login page
    When i entered valid credentials into email and password fields
    And i searched ipod touch product

  Scenario: Add a review for product
    And i clicked on review link and added my review
    Then successfully message should display


    Scenario: Add a review for product
    And i clicked on review link and added my review in words less then 25
    Then proper message should display