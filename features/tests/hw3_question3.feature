# Created by jaeundelio at 7/26/22
Feature: verify empty cart

  Scenario: user can verify empty cart
    Given open target main page
    When click cart button
    Then Verify message is shown
