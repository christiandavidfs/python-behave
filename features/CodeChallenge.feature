@web @duckduckgo
Feature: DuckDuckGo Web Browsing
              As a web surfer,
              I want to find information online,
  So I can learn new things and get tasks done.

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments

        Scenario Outline: Basic DuckDuckGo Search
            Given the DuckDuckGo home page is loaded
             When the user searches for the name "<searchtext>"
             Then results are shown for the column "<searchresult>"
              And results are shown for the column2 "<searchresult2>"
              And an image is visible

        Examples: testing
                  | searchtext     | searchresult | searchresult2 |
                  | Michael Jordan | Wikipedia    | nba.com       |


        Scenario: Change theme
            Given the DuckDuckGo home page is loaded
             When the user goes to the theme section and make changes in themes
             Then the color is dark

        Scenario: Change language to Lingvo
            Given the DuckDuckGo home page is loaded
             When the user goes to the all settings section
              And change the languague
             Then the languague is español (Chile)