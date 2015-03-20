Feature: OnlineFulfillment

  Scenario: add an OnlineFFO
    Given logged in
    And open internal/onlineFulfillment.xhtml
    When type "<ffo>" in "addOffo"
    When press add
    Then i should see <ffo>

  Scenario: remove an OnlineFFO
    Given logged in
    And open internal/onlineFulfillment.xhtml
    When add "Stuff" to onlineFullfillment
    When press remove
    Then i should not see <ffo>

