# Created by jaeundelio at 11/9/2023
Feature: verify empty cart

  Scenario: user can verify empty cart
    Given open target main page
    When click cart button
    Then Verify message is shown