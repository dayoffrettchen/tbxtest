Feature: OnlineFulfillment

  Scenario: add an OnlineFFO
    Given as 'r@nemesese.de' logged in
    Then it should be illegal to call onlineFFO

  Scenario: add an OnlineFFO
    Given logged in
    And open onlineFFO
    When add "Stuff" to onlineFulfillment
    Then there should be Stuff

  Scenario: add two OnlineFFO
    Given logged in
    And open onlineFFO
    When add "Stuff" to onlineFulfillment
    When add "Stuff" to onlineFulfillment
    Then there should one "Stuff"

  Scenario: remove an OnlineFFO
    Given logged in
    And open onlineFFO
    When remove "Stuff" from onlineFulfillment
    Then there should be no "Stuff"

  Scenario: set an ffo
    Given logged in
    And open onlineFFO
    And "Stuff" is added to onlineFulfillment
    And "Stuff2" is added to onlineFulfillment
    When the onlineFFO "Stuff" set "false"
    When the onlineFFO "Stuff2" set "true"
    When save the onlineFFO
    Then the onlineFFO "Stuff" is "false"
    Then the onlineFFO "Stuff2" is "true"

  Scenario: remove all ffos
    Given logged in
    And open onlineFFO
    When all onlineFFO are deleted
    Then no onlineFFO are shown

  Scenario: add ffo in admin page validate on retailer site
    Given logged in
    And open onlineFFO
    When add "newFFO" to onlineFulfillment
    Then ffo "newFFO" is shown on retailerPage

