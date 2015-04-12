Feature: Login

  Scenario: visit tbx
    When logged out
    Then its shows log in Page

  Scenario: visit tbx
    When logged in
    Then i should see Eingeloggt
