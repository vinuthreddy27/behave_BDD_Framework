Feature: Review Functionality


  Scenario: Add a review for product
    Given i navigated to login page
    When i enterd valid credentials into email and password fields
    And i clicked on login button
    And i searched ipod touch product
    And i clicked on review link and added my review
    Then successfull message should display