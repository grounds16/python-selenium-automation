Feature: Search tests
    Scenario: User can search for coffee
        Given Open target main page
        When search for coffee
        Then Verify search worked for coffe
        And Verify coffee in search result url
    Scenario: User can search for tea
        Given Open target main page
        When search for
        Then Verify search worked for coffe
        And Verify coffee in search result url

Scenario Outline: User can search for a product
    Given Open target main page
    When search for <product>
    Then Verify search worked for <expected_product>
    And Verify <expected_url> in search result url
    Examples:
    |product           |expected_product            | expected_url      |
    |coffee            | coffee                     | coffee            |
    |tea               | tea                        | tea               |
    |mug               | mug                        | mug               |
    |christmas lights  | christmas lights           | christmas+lights  |