# In order to avoid leaving my vehicle unsecured, as a vehicle owner, I want all doors to relock if accidently unlock the vehicle

Feature: Auto relocking
    Background:
        Given I do not have an authenticated key with me
        And my vehicle 'locked' with no release buttons pressed

    Scenario Outline: Auto relocking
        When I press the 'unlock' button
        And all doors get 'unlocked'
        And I wait <wait_time> seconds

        Then all doors should be <expected_state>

        Examples:
            | wait_time | expected_state |
            | 10        | unlocked       |
            | 16        | locked         |

    Scenario Outline: Not auto relocking if released button is pressed
        When I press the 'unlock' button
        And all doors get 'unlocked'
        And I 'hold' the door <door_id> release button
        And I 'release' the door <door_id> release button
        And I wait '16' seconds

        Then all doors should be 'unlocked'

        Examples:
            | door_id |
            | 1       |
            | 2       |
            | 3       |
            | 4       |