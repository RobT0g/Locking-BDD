# In order to access my vehicle, as a vehicle owner, I want to unlock a single door by interacting with it while my key is with me

Feature: Unlock individual door
    Background:
        Given I do not have an authenticated key with me
        And my vehicle is 'locked' with no release buttons pressed
        And all doors are 'closed'

    Scenario Outline: Unlocking a single door when I have the key
        Given the door <door_id> is 'locked'
        And I have an authenticated key with me

        When I 'press' the door <door_id> release button

        Then the door <door_id> should be 'unlocked'
        And the door <door_id> should be 'released'

        Examples:
            | door_id |
            | 1       |
            | 2       |
            | 3       |
            | 4       |

    Scenario Outline: Unlocking multiple single doors when I have the key   
        Given all doors are 'locked'
        And I have an authenticated key with me

        When I 'press' the door <door_id_1> release button
        And I 'press' the door <door_id_2> release button

        Then the door <door_id_1> should be 'unlocked'
        And the door <door_id_1> should be 'released'
        And the door <door_id_2> should be 'unlocked'
        And the door <door_id_2> should be 'released'

        Examples:
            | door_id_1 | door_id_2 |
            | 1         | 2         |
            | 1         | 3         |
            | 1         | 4         |
            | 2         | 1         |
            | 2         | 3         |
            | 2         | 4         |
            | 3         | 1         |
            | 3         | 2         |
            | 3         | 4         |
            | 4         | 1         |
            | 4         | 2         |
            | 4         | 3         |

    Scenario Outline: Individual door is left unlocked
        Given the door <door_id> is 'locked'
        And I have an authenticated key with me

        When I 'press' the door <door_id> release button
        And I wait '1' seconds
        And I 'release' the door <door_id> release button

        Then the door <door_id> should be 'unlocked'
        And the door <door_id> should be 'held'

        Examples:
            | door_id |
            | 1       |
            | 2       |
            | 3       |
            | 4       |
