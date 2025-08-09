# In order to avoid leaving my vehicle unsecured, as a vehicle owner, I want all doors to relock if accidently unlock the vehicle

Feature: Auto relocking
    Background:
        Given I do not have an authenticated key with me
        And my vehicle is 'locked' with no release buttons pressed
        And all doors are 'closed'

    Scenario Outline: Auto relocking
        Given all doors are <initial_state>
        And the vehicle 'unlock' button has been pressed

        When I wait <wait_time> seconds

        Then all doors should be <expected_state>

        Examples:
            | initial_state | wait_time | expected_state |
            | locked        | 5         | unlocked       |
            | locked        | 10        | unlocked       |
            | locked        | 14        | unlocked       |
            | locked        | 15        | locked         |
            | locked        | 16        | locked         |
            | unlocked      | 5         | unlocked       |
            | unlocked      | 10        | unlocked       |
            | unlocked      | 14        | unlocked       |
            | unlocked      | 15        | unlocked       |
            | unlocked      | 16        | unlocked       |

    Scenario Outline: Not auto relocking if release button is pressed
        Given all doors are 'locked'
        And the vehicle 'unlock' button has been pressed
        And the release button on door <door_id> is 'released'
        And the release button on door <door_id> is 'pressed'

        When I wait '15' seconds

        Then all doors should be 'unlocked'

        Examples:
            | door_id |
            | 1       |
            | 2       |
            | 3       |
            | 4       |

    Scenario Outline: Not auto relocking if one or more doors are unlocked
        Given the door '1' is <door_1_state>
        And the door '2' is <door_2_state>
        And the door '3' is <door_3_state>
        And the door '4' is <door_4_state>
        And the vehicle 'unlock' button has been pressed

        When I wait '15' seconds

        Then all doors should be <final_state>

        Examples:
            | door_1_state | door_2_state | door_3_state | door_4_state | final_state |
            | unlocked     | unlocked     | unlocked     | unlocked     | unlocked    |
            | unlocked     | unlocked     | unlocked     | locked       | unlocked    |
            | unlocked     | unlocked     | locked       | unlocked     | unlocked    |
            | unlocked     | unlocked     | locked       | locked       | unlocked    |
            | unlocked     | locked       | unlocked     | unlocked     | unlocked    |
            | unlocked     | locked       | unlocked     | locked       | unlocked    |
            | unlocked     | locked       | locked       | unlocked     | unlocked    |
            | unlocked     | locked       | locked       | locked       | unlocked    |
            | locked       | unlocked     | unlocked     | unlocked     | unlocked    |
            | locked       | unlocked     | unlocked     | locked       | unlocked    |
            | locked       | unlocked     | locked       | unlocked     | unlocked    |
            | locked       | unlocked     | locked       | locked       | unlocked    |
            | locked       | locked       | unlocked     | unlocked     | unlocked    |
            | locked       | locked       | unlocked     | locked       | unlocked    |
            | locked       | locked       | locked       | unlocked     | unlocked    |
            | locked       | locked       | locked       | locked       | locked      |

    Scenario: Not auto relocking if unlock button is pressed twice
        Given all doors are 'locked'
        And the vehicle 'unlock' button has been pressed
        And the vehicle 'unlock' button has been pressed

        When I wait '15' seconds

        Then all doors should be 'unlocked'