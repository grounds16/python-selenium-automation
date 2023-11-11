Feature: Search tests
    Scenario: Empty Cart is shown
        Given Open target main page
        When User selects the cart button
        Then Verify Cart is empty

    Scenario: User is able to sign in
        Given Open target main page
        When User selects Signin
        And User selects Signin from the sign menu
        Then Verify Signin Form is displayed

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