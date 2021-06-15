@web @Google
Feature: Shift Left Scenario
              As a web surfer,
              I want to find information online,
  So I can learn new things and get tasks done.

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments

        Scenario: Basic Google Search
            Given the Google home page is displayed
             When the user grab a value from an API
             When the user searches for API
             Then results are shown for API
