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

    Scenario: Verify the amount of benefit cards
        Given User navigates to target circle
        Then Verify there 5 benefit cards are displayed