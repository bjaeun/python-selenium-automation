# Created by jaeundelio at 7/30/22
Feature: cart check

   Scenario: user can add a product to the cart
    Given open amazon page
     When Search for weighted hula hoop on amazon
     And Click on the first product
     And Click on Add to cart button
#     And Open cart page
    Then Verify cart has 1 item