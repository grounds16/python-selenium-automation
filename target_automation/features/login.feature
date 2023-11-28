Feature: Login Page
  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open target main page
     When User selects Signin
     And User selects Signin from the sign menu
     When Store original windows
     And Click on Target terms and conditions link
     And Switch to the newly opened window
     Then Verify Terms and Conditions page is opened
     And User can close new window and switch back to original
