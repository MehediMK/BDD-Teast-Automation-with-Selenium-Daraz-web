Feature: Product price sort and View

    Background: Daraz Website
        Given Open Chrome Browser
        And Browse Daraz Website
    
    Scenario: show product by Traditional Laptops category
        When Type "laptop" search bar
        And Click/Press Enter on Search Button
        And click on "Traditional Laptops" from "Related Categories" area
        Then Close Chrome Browser
    

    Scenario: show product by Gaming Laptops category
        When Type "laptop" search bar
        And Click/Press Enter on Search Button
        And click on "Gaming Laptops" from "Related Categories" area
        Then Close Chrome Browser
    

    Scenario: show product by"Macbooks" related category
        When Type "laptop" search bar
        And Click/Press Enter on Search Button
        And click on "Macbooks" from "Related Categories" area
        Then Close Chrome Browser
    

    Scenario: show product by "Routers" category
        When Type "laptop" search bar
        And Click/Press Enter on Search Button
        And click on "Routers" from "Related Categories" area
        Then Close Chrome Browser
    

    Scenario: show product by related "Basic Micep" category
        When Type "laptop" search bar
        And Click/Press Enter on Search Button
        And click on "Basic Micep" from "Related Categories" area
        Then Close Chrome Browser
    

    Scenario: show product by "Basic" related category
        When Type "laptop" search bar
        And Click/Press Enter on Search Button
        And click on "Basic" from "Related Categories" area
        Then Close Chrome Browser