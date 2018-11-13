Feature: Who is greeting
  Depending on who is actually greeting one should reply properly

  Scenario: Human
    Given I have a proper name
    When I am running the program
    Then Greet as you are supposed to
