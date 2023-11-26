Feature: Cart tests
    Scenario: Empty Cart is shown
        Given Open target main page
        When User selects the cart button
        Then Verify Cart is empty