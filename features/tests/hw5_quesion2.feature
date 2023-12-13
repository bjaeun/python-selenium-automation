# Created by jaeundelio at 11/23/23
Feature: Tests for product page

  Scenario Outline: User can select colors
    Given Open target product <product> page
    Then Verify user can click through colors
    Examples:
    |product      |
    |A-89191279   |
    |A-88345426   |