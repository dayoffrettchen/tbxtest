# Created by christoph at 27.03.15
Feature: the energy effiency class
  # Enter feature description here

  Scenario: Pregiven Energieeffizienklassen
    Given logged in
    When the category "Elektronik & Foto > Einbaugeräte & Großgeräte > Backöfen & Kochfelder" is selected
    Then the attribute "Energieeffizienzklasse" wird angezeigt
    And a drop down with the following entries is shown
      | label           |
      | bitte Auswählen |
      | A+++            |
      | A++             |
      | A+              |
      | A               |
      | B               |
      | C               |
      | D               |
      | E               |
      | F               |
      | G               |


