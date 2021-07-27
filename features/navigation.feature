Feature: As a website user,
            I want all the links to work

  Scenario: Home page > Login
     Given flaskr is setup
      When I click on "Log In"
      Then I should be redirected to the "Log In" page