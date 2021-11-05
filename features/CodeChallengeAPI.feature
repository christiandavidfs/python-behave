@web @Google
Feature: Query DDG to see Image results.

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments

        Scenario: API image response
            Given The API is UP
             When the user gets images list
             Then print results
