Feature: Lock all
    Scenario: Locking all doors with vehicle initially unlocked
        Given my vehicle is 'unlocked'
        When I press the 'lock' button
        Then all doors should be 'locked'

    Scenario Outline: Locking all doors with partial doors initially unlocked
        Given my vehicle door '1' is <door_1_state>
        And my vehicle door '2' is <door_2_state>
        And my vehicle door '3' is <door_3_state>
        And my vehicle door '4' is <door_4_state>
        
        When I press the 'lock' button
        Then all doors should be 'locked'

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
            | locked        | locked        | locked        | unlocked      |
            | locked        | locked        | locked        | locked        |

    Scenario Outline: Door cannot be released when locked
        Given my vehicle door <door_id> is 'locked'
        When I press the door <door_id> release button
        Then all doors should be 'locked'
        And the door <door_id> should be 'held'

        Examples:
            | door_id |
            | 1       |
            | 2       |
            | 3       |
            | 4       |