# In order to ensure my vehicle will not change lock state, as a vehicle owner, I want my vehicle to store the last lock state before turning off

Feature: Storing last lock state
    Background:
        Given I do not have an authenticated key with me
        And my vehicle 'locked' with no release buttons pressed

    Scenario Outline: Saving last state
        Given the door '1' is <door_1_state>
        And the door '2' is <door_2_state>
        And the door '3' is <door_3_state>
        And the door '4' is <door_4_state>

        When I turn off the vehicle
        And I turn on the vehicle

        Then the door '1' should be <door_1_state>
        And the door '2' should be <door_2_state>
        And the door '3' should be <door_3_state>
        And the door '4' should be <door_4_state>

        Examples:
            | door_1_state  | door_2_state  | door_3_state  | door_4_state  |
            | unlocked      | unlocked      | unlocked      | unlocked      |
            | unlocked      | unlocked      | unlocked      | locked        |
            | unlocked      | unlocked      | locked        | unlocked      |
            | unlocked      | unlocked      | locked        | locked        |
            | unlocked      | locked        | unlocked      | unlocked      |
            | unlocked      | locked        | unlocked      | locked        |
            | unlocked      | locked        | locked        | unlocked      |
            | unlocked      | locked        | locked        | locked        |
            | locked        | unlocked      | unlocked      | unlocked      |
            | locked        | unlocked      | unlocked      | locked        |
            | locked        | unlocked      | locked        | unlocked      |
            | locked        | unlocked      | locked        | locked        |
            | locked        | locked        | unlocked      | unlocked      |
            | locked        | locked        | unlocked      | locked        |

    Scenario Outline: Saving the last state immediately after locking/unlocking all doors
        Given the door '1' is <door_1_state>
        And the door '2' is <door_2_state>
        And the door '3' is <door_3_state>
        And the door '4' is <door_4_state>

        When I press the <operation_button> button
        And I turn off the vehicle
        And I turn on the vehicle

        Then all doors should be <operation_state>

        Examples:
            | door_1_state  | door_2_state  | door_3_state  | door_4_state  | operation_button | operation_state |
            | unlocked      | unlocked      | unlocked      | unlocked      | lock             | locked          |
            | unlocked      | unlocked      | unlocked      | locked        | lock             | locked          |
            | unlocked      | unlocked      | locked        | unlocked      | lock             | locked          |
            | unlocked      | unlocked      | locked        | locked        | lock             | locked          |
            | unlocked      | locked        | unlocked      | unlocked      | lock             | locked          |
            | unlocked      | locked        | unlocked      | locked        | lock             | locked          |
            | unlocked      | locked        | locked        | unlocked      | lock             | locked          |
            | unlocked      | locked        | locked        | locked        | lock             | locked          |
            | locked        | unlocked      | unlocked      | unlocked      | lock             | locked          |
            | locked        | unlocked      | unlocked      | locked        | lock             | locked          |
            | locked        | unlocked      | locked        | unlocked      | lock             | locked          |
            | locked        | unlocked      | locked        | locked        | lock             | locked          |
            | locked        | locked        | unlocked      | unlocked      | lock             | locked          |
            | locked        | locked        | unlocked      | locked        | lock             | locked          |
            | locked        | locked        | locked        | unlocked      | lock             | locked          |
            | locked        | locked        | locked        | locked        | lock             | locked          |
            | unlocked      | unlocked      | unlocked      | unlocked      | unlock           | unlocked        |
            | unlocked      | unlocked      | unlocked      | locked        | unlock           | unlocked        |
            | unlocked      | unlocked      | locked        | unlocked      | unlock           | unlocked        |
            | unlocked      | unlocked      | locked        | locked        | unlock           | unlocked        |
            | unlocked      | locked        | unlocked      | unlocked      | unlock           | unlocked        |
            | unlocked      | locked        | unlocked      | locked        | unlock           | unlocked        |
            | unlocked      | locked        | locked        | unlocked      | unlock           | unlocked        |
            | unlocked      | locked        | locked        | locked        | unlock           | unlocked        |
            | locked        | unlocked      | unlocked      | unlocked      | unlock           | unlocked        |
            | locked        | unlocked      | unlocked      | locked        | unlock           | unlocked        |
            | locked        | unlocked      | locked        | unlocked      | unlock           | unlocked        |
            | locked        | unlocked      | locked        | locked        | unlock           | unlocked        |
            | locked        | locked        | unlocked      | unlocked      | unlock           | unlocked        |
            | locked        | locked        | unlocked      | locked        | unlock           | unlocked        |
            | locked        | locked        | locked        | unlocked      | unlock           | unlocked        |
            | locked        | locked        | locked        | locked        | unlock           | unlocked        |

    Scenario Outline: Saving the last state immediately after unlocking individual doors
        Given the door <door_id> is 'locked'
        And I have an authenticated key with me

        When I press the door <door_id> release button
        And I wait '1' seconds
        And I release the door <door_id> release button
        And I turn off the vehicle
        And I turn on the vehicle

        Then the door <door_id> should be 'unlocked'

        Examples:
            | door_id |
            | 1       |
            | 2       |
            | 3       |
            | 4       |

    Scenario Outline: Saving the last state immediately after auto-relocking
        Given the door '1' is <door_1_state>
        And the door '2' is <door_2_state>
        And the door '3' is <door_3_state>
        And the door '4' is <door_4_state>

        When I press the 'unlock' button
        And all doors get 'unlocked'
        And I wait <wait_time> seconds
        And I turn off the vehicle
        And I turn on the vehicle

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
