# In order to avoid leaving my vehicle unsecured, as a vehicle owner, I want all doors to relock if accidently unlock the vehicle

Feature: Auto relocking
    Background:
        Given I do not have an authenticated key with me
        And my vehicle 'locked' with no release buttons pressed

    Scenario Outline: Auto relocking
        Given the door '1' is <door_1_state>
        And the door '2' is <door_2_state>
        And the door '3' is <door_3_state>
        And the door '4' is <door_4_state>

        When I press the 'unlock' button
        And all doors get 'unlocked'
        And I wait <wait_time> seconds

        Then all doors should be <expected_state>

        Examples:
            | door_1_state  | door_2_state  | door_3_state  | door_4_state  | wait_time | expected_state |
            | unlocked      | unlocked      | unlocked      | unlocked      | 10        | unlocked       |
            | unlocked      | unlocked      | unlocked      | locked        | 10        | unlocked       |
            | unlocked      | unlocked      | locked        | unlocked      | 10        | unlocked       |
            | unlocked      | unlocked      | locked        | locked        | 10        | unlocked       |
            | unlocked      | locked        | unlocked      | unlocked      | 10        | unlocked       |
            | unlocked      | locked        | unlocked      | locked        | 10        | unlocked       |
            | unlocked      | locked        | locked        | unlocked      | 10        | unlocked       |
            | unlocked      | locked        | locked        | locked        | 10        | unlocked       |
            | locked        | unlocked      | unlocked      | unlocked      | 10        | unlocked       |
            | locked        | unlocked      | unlocked      | locked        | 10        | unlocked       |
            | locked        | unlocked      | locked        | unlocked      | 10        | unlocked       |
            | locked        | unlocked      | locked        | locked        | 10        | unlocked       |
            | locked        | locked        | unlocked      | unlocked      | 10        | unlocked       |
            | locked        | locked        | unlocked      | locked        | 10        | unlocked       |
            | locked        | locked        | locked        | unlocked      | 10        | unlocked       |
            | locked        | locked        | locked        | locked        | 10        | unlocked       |
            | unlocked      | unlocked      | unlocked      | unlocked      | 16        | locked         |
            | unlocked      | unlocked      | unlocked      | locked        | 16        | locked         |
            | unlocked      | unlocked      | locked        | unlocked      | 16        | locked         |
            | unlocked      | unlocked      | locked        | locked        | 16        | locked         |
            | unlocked      | locked        | unlocked      | unlocked      | 16        | locked         |
            | unlocked      | locked        | unlocked      | locked        | 16        | locked         |
            | unlocked      | locked        | locked        | unlocked      | 16        | locked         |
            | unlocked      | locked        | locked        | locked        | 16        | locked         |
            | locked        | unlocked      | unlocked      | unlocked      | 16        | locked         |
            | locked        | unlocked      | unlocked      | locked        | 16        | locked         |
            | locked        | unlocked      | locked        | unlocked      | 16        | locked         |
            | locked        | unlocked      | locked        | locked        | 16        | locked         |
            | locked        | locked        | unlocked      | unlocked      | 16        | locked         |
            | locked        | locked        | unlocked      | locked        | 16        | locked         |
            | locked        | locked        | locked        | unlocked      | 16        | locked         |
            | locked        | locked        | locked        | locked        | 16        | locked         |

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