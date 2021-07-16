Feature: Daraz Product Search

    Background: Open Browser
        Given Open Chrome Browser
        And Browse Daraz Website


    Scenario: Search with empty value
        When Type "" search bar
        And Click/Press Enter on Search Button
        Then Close Chrome Browser


    Scenario: Search with product name
        When Type "laptop" search bar
        And Click/Press Enter on Search Button
        Then Close Chrome Browser


    Scenario: Search with different product name
        When Type "samsung mobile phone" search bar
        And Click/Press Enter on Search Button
        Then Close Chrome Browser


    Scenario: Count Search product in first page
        When Type "samsung mobile phone" search bar
        And Click/Press Enter on Search Button
        And Count all product in first page
        Then Close Chrome Browser


    Scenario: Get total search item found
        When Type "laptop" search bar
        And Click/Press Enter on Search Button
        And Assert how many items found
        And Get total search item found
        Then Close Chrome Browser

    