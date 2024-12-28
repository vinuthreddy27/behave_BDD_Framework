Feature: Register Functionality

  Scenario: user should login
     Given i navigated to register page
     When i validated the page title
     And i enter detail into name textfield
     And i clicked on submit button
     Then user should login successfully

 @rp
  Scenario: alternative way to reach register page

    And  i clicked on continue btn
    Then register page should display

   @rp1
    Scenario: alternative way to reach register page
    Then   i enter valid credentials into respective textfield
    And  i clicked on register link
    Then register page should display