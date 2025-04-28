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
            | unlocked      | unlocked      | unlocked      | unlocked      | 20        | unlocked       |
            | unlocked      | unlocked      | unlocked      | locked        | 20        | unlocked       |
            | unlocked      | unlocked      | locked        | unlocked      | 20        | unlocked       |
            | unlocked      | unlocked      | locked        | locked        | 20        | unlocked       |
            | unlocked      | locked        | unlocked      | unlocked      | 20        | unlocked       |
            | unlocked      | locked        | unlocked      | locked        | 20        | unlocked       |
            | unlocked      | locked        | locked        | unlocked      | 20        | unlocked       |
            | unlocked      | locked        | locked        | locked        | 20        | unlocked       |
            | locked        | unlocked      | unlocked      | unlocked      | 20        | unlocked       |
            | locked        | unlocked      | unlocked      | locked        | 20        | unlocked       |
            | locked        | unlocked      | locked        | unlocked      | 20        | unlocked       |
            | locked        | unlocked      | locked        | locked        | 20        | unlocked       |
            | locked        | locked        | unlocked      | unlocked      | 20        | unlocked       |
            | locked        | locked        | unlocked      | locked        | 20        | unlocked       |
            | locked        | locked        | locked        | unlocked      | 20        | unlocked       |
            | locked        | locked        | locked        | locked        | 20        | unlocked       |
            | unlocked      | unlocked      | unlocked      | unlocked      | 30        | locked         |
            | unlocked      | unlocked      | unlocked      | locked        | 30        | locked         |
            | unlocked      | unlocked      | locked        | unlocked      | 30        | locked         |
            | unlocked      | unlocked      | locked        | locked        | 30        | locked         |
            | unlocked      | locked        | unlocked      | unlocked      | 30        | locked         |
            | unlocked      | locked        | unlocked      | locked        | 30        | locked         |
            | unlocked      | locked        | locked        | unlocked      | 30        | locked         |
            | unlocked      | locked        | locked        | locked        | 30        | locked         |
            | locked        | unlocked      | unlocked      | unlocked      | 30        | locked         |
            | locked        | unlocked      | unlocked      | locked        | 30        | locked         |
            | locked        | unlocked      | locked        | unlocked      | 30        | locked         |
            | locked        | unlocked      | locked        | locked        | 30        | locked         |
            | locked        | locked        | unlocked      | unlocked      | 30        | locked         |
            | locked        | locked        | unlocked      | locked        | 30        | locked         |
            | locked        | locked        | locked        | unlocked      | 30        | locked         |
            | locked        | locked        | locked        | locked        | 30        | locked         |

    Scenario Outline: Not auto relocking if released button is pressed
        Given the door '1' is <door_1_state>
        And the door '2' is <door_2_state>
        And the door '3' is <door_3_state>
        And the door '4' is <door_4_state>

        When I press the 'unlock' button
        And all doors get 'unlocked'
        And I press the door <door_id> release button
        And I wait <wait_time> seconds

        Then all doors should be 'unlocked'

        Examples:
            | door_1_state  | door_2_state  | door_3_state  | door_4_state  | door_id | wait_time |
            | unlocked      | unlocked      | unlocked      | unlocked      | 1       | 30        |
            | unlocked      | unlocked      | unlocked      | unlocked      | 2       | 30        |
            | unlocked      | unlocked      | unlocked      | unlocked      | 3       | 30        |
            | unlocked      | unlocked      | unlocked      | unlocked      | 4       | 30        |
            | unlocked      | unlocked      | unlocked      | locked        | 1       | 30        |
            | unlocked      | unlocked      | unlocked      | locked        | 2       | 30        |
            | unlocked      | unlocked      | unlocked      | locked        | 3       | 30        |
            | unlocked      | unlocked      | unlocked      | locked        | 4       | 30        |
            | unlocked      | unlocked      | locked        | unlocked      | 1       | 30        |
            | unlocked      | unlocked      | locked        | unlocked      | 2       | 30        |
            | unlocked      | unlocked      | locked        | unlocked      | 3       | 30        |
            | unlocked      | unlocked      | locked        | unlocked      | 4       | 30        |
            | unlocked      | unlocked      | locked        | locked        | 1       | 30        |
            | unlocked      | unlocked      | locked        | locked        | 2       | 30        |
            | unlocked      | unlocked      | locked        | locked        | 3       | 30        |
            | unlocked      | unlocked      | locked        | locked        | 4       | 30        |
            | unlocked      | locked        | unlocked      | unlocked      | 1       | 30        |
            | unlocked      | locked        | unlocked      | unlocked      | 2       | 30        |
            | unlocked      | locked        | unlocked      | unlocked      | 3       | 30        |
            | unlocked      | locked        | unlocked      | unlocked      | 4       | 30        |
            | unlocked      | locked        | unlocked      | locked        | 1       | 30        |
            | unlocked      | locked        | unlocked      | locked        | 2       | 30        |
            | unlocked      | locked        | unlocked      | locked        | 3       | 30        |
            | unlocked      | locked        | unlocked      | locked        | 4       | 30        |
            | unlocked      | locked        | locked        | unlocked      | 1       | 30        |
            | unlocked      | locked        | locked        | unlocked      | 2       | 30        |
            | unlocked      | locked        | locked        | unlocked      | 3       | 30        |
            | unlocked      | locked        | locked        | unlocked      | 4       | 30        |
            | unlocked      | locked        | locked        | locked        | 1       | 30        |
            | unlocked      | locked        | locked        | locked        | 2       | 30        |
            | unlocked      | locked        | locked        | locked        | 3       | 30        |
            | unlocked      | locked        | locked        | locked        | 4       | 30        |
            | locked        | unlocked      | unlocked      | unlocked      | 1       | 30        |
            | locked        | unlocked      | unlocked      | unlocked      | 2       | 30        |
            | locked        | unlocked      | unlocked      | unlocked      | 3       | 30        |
            | locked        | unlocked      | unlocked      | unlocked      | 4       | 30        |
            | locked        | unlocked      | unlocked      | locked        | 1       | 30        |
            | locked        | unlocked      | unlocked      | locked        | 2       | 30        |
            | locked        | unlocked      | unlocked      | locked        | 3       | 30        |
            | locked        | unlocked      | unlocked      | locked        | 4       | 30        |
            | locked        | unlocked      | locked        | unlocked      | 1       | 30        |
            | locked        | unlocked      | locked        | unlocked      | 2       | 30        |
            | locked        | unlocked      | locked        | unlocked      | 3       | 30        |
            | locked        | unlocked      | locked        | unlocked      | 4       | 30        |
            | locked        | unlocked      | locked        | locked        | 1       | 30        |
            | locked        | unlocked      | locked        | locked        | 2       | 30        |
            | locked        | unlocked      | locked        | locked        | 3       | 30        |
            | locked        | unlocked      | locked        | locked        | 4       | 30        |
            | locked        | locked        | unlocked      | unlocked      | 1       | 30        |
            | locked        | locked        | unlocked      | unlocked      | 2       | 30        |
            | locked        | locked        | unlocked      | unlocked      | 3       | 30        |
            | locked        | locked        | unlocked      | unlocked      | 4       | 30        |
            | locked        | locked        | unlocked      | locked        | 1       | 30        |
            | locked        | locked        | unlocked      | locked        | 2       | 30        |
            | locked        | locked        | unlocked      | locked        | 3       | 30        |
            | locked        | locked        | unlocked      | locked        | 4       | 30        |
            | locked        | locked        | locked        | unlocked      | 1       | 30        |
            | locked        | locked        | locked        | unlocked      | 2       | 30        |
            | locked        | locked        | locked        | unlocked      | 3       | 30        |
            | locked        | locked        | locked        | unlocked      | 4       | 30        |
            | locked        | locked        | locked        | locked        | 1       | 30        |
            | locked        | locked        | locked        | locked        | 2       | 30        |
            | locked        | locked        | locked        | locked        | 3       | 30        |
            | locked        | locked        | locked        | locked        | 4       | 30        |
            | unlocked      | unlocked      | unlocked      | unlocked      | 1       | 40        |
            | unlocked      | unlocked      | unlocked      | unlocked      | 2       | 40        |
            | unlocked      | unlocked      | unlocked      | unlocked      | 3       | 40        |
            | unlocked      | unlocked      | unlocked      | unlocked      | 4       | 40        |
            | unlocked      | unlocked      | unlocked      | locked        | 1       | 40        |
            | unlocked      | unlocked      | unlocked      | locked        | 2       | 40        |
            | unlocked      | unlocked      | unlocked      | locked        | 3       | 40        |
            | unlocked      | unlocked      | unlocked      | locked        | 4       | 40        |
            | unlocked      | unlocked      | locked        | unlocked      | 1       | 40        |
            | unlocked      | unlocked      | locked        | unlocked      | 2       | 40        |
            | unlocked      | unlocked      | locked        | unlocked      | 3       | 40        |
            | unlocked      | unlocked      | locked        | unlocked      | 4       | 40        |
            | unlocked      | unlocked      | locked        | locked        | 1       | 40        |
            | unlocked      | unlocked      | locked        | locked        | 2       | 40        |
            | unlocked      | unlocked      | locked        | locked        | 3       | 40        |
            | unlocked      | unlocked      | locked        | locked        | 4       | 40        |
            | unlocked      | locked        | unlocked      | unlocked      | 1       | 40        |
            | unlocked      | locked        | unlocked      | unlocked      | 2       | 40        |
            | unlocked      | locked        | unlocked      | unlocked      | 3       | 40        |
            | unlocked      | locked        | unlocked      | unlocked      | 4       | 40        |
            | unlocked      | locked        | unlocked      | locked        | 1       | 40        |
            | unlocked      | locked        | unlocked      | locked        | 2       | 40        |
            | unlocked      | locked        | unlocked      | locked        | 3       | 40        |
            | unlocked      | locked        | unlocked      | locked        | 4       | 40        |
            | unlocked      | locked        | locked        | unlocked      | 1       | 40        |
            | unlocked      | locked        | locked        | unlocked      | 2       | 40        |
            | unlocked      | locked        | locked        | unlocked      | 3       | 40        |
            | unlocked      | locked        | locked        | unlocked      | 4       | 40        |
            | unlocked      | locked        | locked        | locked        | 1       | 40        |
            | unlocked      | locked        | locked        | locked        | 2       | 40        |
            | unlocked      | locked        | locked        | locked        | 3       | 40        |
            | unlocked      | locked        | locked        | locked        | 4       | 40        |
            | locked        | unlocked      | unlocked      | unlocked      | 1       | 40        |
            | locked        | unlocked      | unlocked      | unlocked      | 2       | 40        |
            | locked        | unlocked      | unlocked      | unlocked      | 3       | 40        |
            | locked        | unlocked      | unlocked      | unlocked      | 4       | 40        |
            | locked        | unlocked      | unlocked      | locked        | 1       | 40        |
            | locked        | unlocked      | unlocked      | locked        | 2       | 40        |
            | locked        | unlocked      | unlocked      | locked        | 3       | 40        |
            | locked        | unlocked      | unlocked      | locked        | 4       | 40        |
            | locked        | unlocked      | locked        | unlocked      | 1       | 40        |
            | locked        | unlocked      | locked        | unlocked      | 2       | 40        |
            | locked        | unlocked      | locked        | unlocked      | 3       | 40        |
            | locked        | unlocked      | locked        | unlocked      | 4       | 40        |
            | locked        | unlocked      | locked        | locked        | 1       | 40        |
            | locked        | unlocked      | locked        | locked        | 2       | 40        |
            | locked        | unlocked      | locked        | locked        | 3       | 40        |
            | locked        | unlocked      | locked        | locked        | 4       | 40        |
            | locked        | locked        | unlocked      | unlocked      | 1       | 40        |
            | locked        | locked        | unlocked      | unlocked      | 2       | 40        |
            | locked        | locked        | unlocked      | unlocked      | 3       | 40        |
            | locked        | locked        | unlocked      | unlocked      | 4       | 40        |
            | locked        | locked        | unlocked      | locked        | 1       | 40        |
            | locked        | locked        | unlocked      | locked        | 2       | 40        |
            | locked        | locked        | unlocked      | locked        | 3       | 40        |
            | locked        | locked        | unlocked      | locked        | 4       | 40        |
            | locked        | locked        | locked        | unlocked      | 1       | 40        |
            | locked        | locked        | locked        | unlocked      | 2       | 40        |
            | locked        | locked        | locked        | unlocked      | 3       | 40        |
            | locked        | locked        | locked        | unlocked      | 4       | 40        |
            | locked        | locked        | locked        | locked        | 1       | 40        |
            | locked        | locked        | locked        | locked        | 2       | 40        |
            | locked        | locked        | locked        | locked        | 3       | 40        |
            | locked        | locked        | locked        | locked        | 4       | 40        |