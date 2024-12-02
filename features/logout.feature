Feature: Logout functionality

  Scenario: user should logout
     Given i navigated to the homepage
     When i validate page title
     And i enter valid credentials into respective textfield
     And i clicked on logout link
    Then proper message should display on logout