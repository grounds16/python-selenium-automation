Feature: Search tests
    Scenario: User can search for coffee
        Given Open target main page
        When search for coffee
        Then Verify search worked for coffee
        And Verify coffee in search result url

    Scenario: User can search for products
        Given Open target main page
        When search for tea
        Then Verify search worked for tea
        And Verify tea in search result url

    Scenario: User can add to cart
        Given Open target main page
        When search for AirPods (3rd Generation)
        Then Verify item is found and select cart
        When User selects the cart button
        Then Verify item is in cart

    Scenario: Verify colors on products
        Given User navigates to shirt page
        Then Verify colors matches title



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