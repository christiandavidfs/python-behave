Feature: showing off behave

  Scenario: run a simple test false
     Given we have behave installed
      When we implement a test
      Then behave will test it for us as false!

    Scenario: run a simple test true
     Given we have behave installed
      When we implement a test
      Then behave will test it for us as true!