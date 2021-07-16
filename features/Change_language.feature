Feature: Change language

    Background: Daraz Website
        Given Open Chrome Browser
        And Browse Daraz Website


    Scenario: Change Language english to bangla
        When Click on "ভাষা" link from top menu bar
        And Click on "BN / Bengali" 
        Then Close Browser


    Scenario: Change Language english to bangla
        When Click on "ভাষা" link from top menu bar
        And Click on "BN / Bengali" 
        And Click on "CHANGE LANGUAGE" link from top menu bar
        And Click on "EN / English"
        Then Close Browser
