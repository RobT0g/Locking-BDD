# In order to avoid leaving my vehicle unsecured, as a vehicle owner, I want all doors to relock if accidently unlock the vehicle

Feature: Auto relocking
    Background:
        Given I do not have an authenticated key with me
        And my vehicle is 'locked' with no release buttons pressed
        And all doors are 'closed'

    Scenario Outline: Auto relocking
        Given all doors are <initial_state>
        And the vehicle 'unlock' button is 'released'
        And the vehicle 'unlock' button is 'pressed'

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
        And the vehicle 'unlock' button is 'released'
        And the vehicle 'unlock' button is 'pressed'
        And the door <door_id> release button is 'pressed'
        And the door <door_id> release button is 'released'

        When I wait '16' seconds

        Then all doors should be 'unlocked'

        Examples:
            | door_id |
            | 1       |
            | 2       |
            | 3       |
            | 4       |

    Scenario Outline: Not auto relocking if one door is unlocked
        Given  all doors are 'closed'
        And the door <door_id> is 'unlocked'
        And the vehicle 'unlock' button is 'released'
        And the vehicle 'unlock' button is 'pressed'

        When I wait '16' seconds

        Then all doors should be 'unlocked'

        Examples:
            | door_id |
            | 1       |
            | 2       |
            | 3       |
            | 4       |

    Scenario: Not auto relocking if unlock button is pressed twice
        Given all doors are 'locked'
        And the vehicle 'unlock' button is 'released'
        And the vehicle 'unlock' button is 'pressed'
        And the vehicle 'unlock' button is 'released'
        And the vehicle 'unlock' button is 'pressed'

        When I wait '16' seconds

        Then all doors should be 'unlocked'