# In order to avoid leaving my vehicle unsecured, as a vehicle owner, I want all doors to relock if accidently unlock the vehicle

Feature: Auto relocking
    Background:
        Given I do not have an authenticated key with me
        And my vehicle is 'locked' with no release buttons pressed
        And all doors are 'closed'
        And the locking system is 'operational'

    Scenario Outline: Auto relocking
        Given all doors are <initial_state>

        When I press the 'unlock' button
        And all doors get 'unlocked'
        And I wait <wait_time> seconds

        Then all doors should be <expected_state>

        Examples:
            | initial_state | wait_time | expected_state |
            | locked        | 10        | unlocked       |
            | locked        | 16        | locked         |
            | unlocked      | 16        | unlocked       |

    Scenario Outline: Not auto relocking if one door is unlocked
        Given the door <door_id> is 'unlocked'

        When I press the 'unlock' button
        And all doors get 'unlocked'
        And I wait '16' seconds

        Then all doors should be 'unlocked'

        Examples:
            | door_id |
            | 1       |
            | 2       |
            | 3       |
            | 4       |

    Scenario Outline: Not auto relocking if release button is pressed
        Given all doors are 'locked'

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

    Scenario: Not auto relocking if unlock button is pressed twice
        Given all doors are 'locked'

        When I press the 'unlock' button
        And all doors get 'unlocked'
        And I press the 'unlock' button
        And I wait '16' seconds

        Then all doors should be 'unlocked'