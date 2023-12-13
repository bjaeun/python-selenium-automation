# Created by jaeundelio at 11/28/23
Feature: Cart Test Cases
  # Enter feature description here

  Scenario: “Your cart is empty” message is shown for empty cart
    Given open target main page
    When click cart button
    Then Verify message is shown
