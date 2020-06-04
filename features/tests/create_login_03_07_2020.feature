# Created by rapid at 3/7/2020
Feature: Creation of a new account

  Scenario: Creating the new account
    Given Loginpage
    Then Click MY ACCOUNT button
    Then Click Sign In button
    Then Click on Create an account tab
    Then Input First Name FirstName
    Then Input Last Name LastName
    Then Input Telephone 4074354433
    Then Input Mobile 4074354433
    Then Input Account Name FirstName LastName
    Then Input Email Address sanoy2006@fake12.ru
    Then Input Password Password_Test
    Then Confirm Password Password_Test
    Then Input Address 6058 SW 18TH ST APT 4
    Then Choose Country United States of America
    Then Input Zipcode 33023
    Then Choose State/Sity Fl, Hollywood
    Then Click on Create Account button
    Then Verify that text is here: As an essential business, we are open and shipping as usual!