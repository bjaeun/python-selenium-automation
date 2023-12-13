# Created by jaeundelio at 11/23/23

Feature: search result has a name and image

  Scenario Outline: Verify user can see product names and images
    Given Open target main page
    When Search for <product>
    Then Verify every product has a name and image
    Examples:
      | product        | expected_product
      | christmas tree | christmas tree
