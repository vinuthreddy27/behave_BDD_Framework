Feature: affiliate functionality

  Scenario: change necessary details
      Given i navigated to the homepage
      When i validated page title
      And i entered email and password into textfields
      And  i clicked on edit affiliate link
      And do neceassary changes
      Then successfully changed message should display