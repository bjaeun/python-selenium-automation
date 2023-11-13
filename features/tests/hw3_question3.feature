# Created by jaeundelio at 11/10/23
Feature: verify empty cart

  Scenario: user user can access Sign In
    Given open target main page
    When click sign in
    Then Verify Sign In form opened
