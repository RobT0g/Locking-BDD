Feature: Locking Feedback
    Background:
        Given I do not have an authenticated key with me
        And my vehicle is 'locked' with no release buttons pressed
        And all doors are 'closed'

    Scenario Outline: Locking feedback when locking or unlocking the vehicle
        When I press the <operation> button

        Then all doors should be <state>
        And I should receive a <feedback> feedback within '500' ms

        Examples:
            | operation | state    | feedback               |
            | lock      | locked   | locking confirmation   |
            | unlock    | unlocked | unlocking confirmation |

    Scenario Outline: Failure feedback when trying to lock the vehicle with one door open
        Given the door <door_id> is 'unlocked'
        And the door <door_id> is <door_open_state>

        When I press the 'lock' button

        Then all doors should be 'locked'
        And I should receive a <feedback_received> feedback within '500' ms

        Examples:
            | door_id | door_open_state | feedback_received    |
            | 1       | open            | operation failed     |
            | 2       | open            | operation failed     |
            | 3       | open            | operation failed     |
            | 4       | open            | operation failed     |
            | 1       | closed          | locking confirmation |
            | 2       | closed          | locking confirmation |
            | 3       | closed          | locking confirmation |
            | 4       | closed          | locking confirmation |
