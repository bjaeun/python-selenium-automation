# Created by jaeundelio at 12/7/23
Feature: # Enter feature name here
  # Enter feature description here

Scenario: User can open and close Terms and Conditions from sign in page
 Given Open sign in page
 When Store original windows
 And Click on Target terms and conditions link (*see image below)
 And Switch to the newly opened window
 Then Verify Terms and Conditions page is opened
 And User can close new window and switch back to original