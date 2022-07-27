# Created by jaeundelio at 7/26/22
Feature: sign in page

  Scenario: user can see the sign in page
    Given open amazon main page
    When click orders button
    Then Verify the sign in page open
