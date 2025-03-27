Feature: Lock all
    Scenario: Locking all doors with vehicle initially unlocked
        Given my vehicle is unlocked
        When I press the lock button
        Then all doors should be 'locked'