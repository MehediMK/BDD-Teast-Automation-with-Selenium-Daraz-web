Feature: Product price sort and View

    Background: Daraz Website
        Given Open Chrome Browser
        And Browse Daraz Website
    
    Scenario: product sort by "price low to heigh"
        When Type "laptop" search bar
        And Click/Press Enter on Search Button
        And Select/click on "Price low to heigh" from "Short By" area 
        Then Close Chrome Browser
    
    Scenario: Search product sort heigh price to low price
        When Type "laptop" search bar
        And Click/Press Enter on Search Button
        And Select/click on  "Price heigh to low" from "Short By" area 
        Then Close Chrome Browser
    
    Scenario: product sort by "Bast Match"
        When Type "laptop" search bar
        And Click/Press Enter on Search Button
        And Select/click on "Bast Match" from "Short By" area 
        Then Close Chrome Browser

    
    Scenario: Change product  list view
        When Type "laptop" search bar
        And Click/Press Enter on Search Button
        And click on "list view icon" from "View" area
        Then Close Chrome Browser


    Scenario: Change product  list view
        When Type "laptop" search bar
        And Click/Press Enter on Search Button
        And click on "grid view icon" from "View" area
        Then Close Chrome Browser
