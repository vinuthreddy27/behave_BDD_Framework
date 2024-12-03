Feature: Register Functionality



  Scenario: user should login
     Given i navigated to register page
     Then i validated the page title
     Then i enter detail into name textfield
     When i clicked on submit button
     And user should login successfully

 @rp
  Scenario: alternative way to reach register page

    And  i clicked on continue btn
    Then register page should display

   @rp1
    Scenario: alternative way to reach register page
   Then   i enter valid credentials into respective textfield
    And  i clicked on register link
    Then register page should display