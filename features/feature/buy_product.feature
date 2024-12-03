Feature: Buy product from the site

  Background:
     Given i navigated to the homepage
     Then i validated page title
     And i entered email and password into textfields
     And i entered a product name into respective field
     And i clicked on the wishlist btn


  Scenario:add product to wishlist from wishlist buy product
     Then product should be added to wishlist

  Scenario:add product to wishlist from wishlist remove product

     And  i clik on wishlist and remove product from wishlist
     Then product should be removed from  wishlist