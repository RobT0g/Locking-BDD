Feature: Locking Feedback
    Background:
        Given I do not have an authenticated key with me
        And my vehicle is 'locked' with no release buttons pressed
        And all doors are 'closed'

    Scenario: Lock feedback when locking the vehicle
        When I press the 'lock' button

        Then all doors should be 'locked'
        And I should receive a 'locking confirmation' feedback within '500' ms

    Scenario: Unlock feedback when unlocking the vehicle
        When I press the 'unlock' button

        Then all doors should be 'unlocked'
        And I should receive a 'unlocking confirmation' feedback within '500' ms

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
