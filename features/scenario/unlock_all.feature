# In order to access my vehicle, as a vehicle owner, I want to unlock all doors

Feature: Unlock all
    Background:
        Given I do not have an authenticated key with me
        And my vehicle 'locked' with no release buttons pressed

    # Scenario Outline: Unlocking all doors
    #     Given the door '1' is <door_1_state>
    #     And the door '2' is <door_2_state>
    #     And the door '3' is <door_3_state>
    #     And the door '4' is <door_4_state>

    #     When I press the 'unlock' button
    #     Then all doors should be 'unlocked'

    #     Examples:
    #         | door_1_state  | door_2_state  | door_3_state  | door_4_state  |
    #         | unlocked      | unlocked      | unlocked      | unlocked      |
    #         | unlocked      | unlocked      | unlocked      | locked        |
    #         | unlocked      | unlocked      | locked        | unlocked      |
    #         | unlocked      | unlocked      | locked        | locked        |
    #         | unlocked      | locked        | unlocked      | unlocked      |
    #         | unlocked      | locked        | unlocked      | locked        |
    #         | unlocked      | locked        | locked        | unlocked      |
    #         | unlocked      | locked        | locked        | locked        |
    #         | locked        | unlocked      | unlocked      | unlocked      |
    #         | locked        | unlocked      | unlocked      | locked        |
    #         | locked        | unlocked      | locked        | unlocked      |
    #         | locked        | unlocked      | locked        | locked        |
    #         | locked        | locked        | unlocked      | unlocked      |
    #         | locked        | locked        | unlocked      | locked        |
    #         | locked        | locked        | locked        | unlocked      |
    #         | locked        | locked        | locked        | locked        |

    Scenario Outline: Door can be released when unlocked
        Given the door <door_id> is 'unlocked'
        When I 'hold' the door <door_id> release button
        Then the door <door_id> should be 'released'

        Examples:
            | door_id |
            | 1       |
            | 2       |
            | 3       |
            | 4       |
