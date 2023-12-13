# Created by jaeundelio at 11/29/23
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: verify that logged out user can access Sign In
    Given Open target main page
    When Click Sign In
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened


