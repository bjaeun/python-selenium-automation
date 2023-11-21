# Created by jaeundelio at 11/15/2023
Feature: cart check

   Scenario: user can add a product to the cart
     Given open target circle page
     When Search for tv on target
     And Click on Add to cart button
     And Click on Add to cart button from right side navigation menu
#     And Open cart page
     Then Verify cart has 1 item