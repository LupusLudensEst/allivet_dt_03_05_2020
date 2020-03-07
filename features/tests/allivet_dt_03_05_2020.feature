# Created by rapid at 2/4/2020
Feature: Wrong email and password lead to 'Invalid Login' text

  Scenario: Verify that wrong email and password lead to 'Invalid Login' text
    Given Loginpage
    Then Click MY ACCOUNT button
    Then Click Sign In button
    Then Input into e-mail field TestEmail@gmail.com
    Then Input into password field TestPassword
    Then Click login button
    Then Verify page has a text 'Invalid Login'