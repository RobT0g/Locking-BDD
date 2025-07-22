Feature: Locking Feedback
    Background:
        Given I do not have an authenticated key with me
        And my vehicle is 'locked' with no release buttons pressed

    Scenario: Lock feedback when locking the vehicle
        When I press the 'lock' button

        Then all doors should be 'locked'
        And I should receive a 'locking confirmation' feedback within '500' ms

    Scenario: Unlock feedback when unlocking the vehicle
        When I press the 'unlock' button

        Then all doors should be 'unlocked'
        And I should receive a 'unlocking confirmation' feedback within '500' ms

    # Scenario Outline: Failure feedback when trying to lock the vehicle with one door open
    #     Given the door <door_id> is 'unlocked'
    #     And the door <door_id> is 'open'

    #     When I press the 'lock' button

    #     Then all doors should be 'locked'
    #     And I should receive a 'locking failed' feedback within '500' ms

    #     Examples:
    #         | door_id |
    #         | 1       |
    #         | 2       |
    #         | 3       |
    #         | 4       |

    # Scenario Outline: Failure feedback when the vehicle failed to lock the doors
    #     Given all doors are 'unlocked'
    #     And there is a failure in the locking system

    #     When I press the 'lock' button

    #     Then all doors should be 'unlocked'
    #     And I should receive a 'locking failed' feedback within '500' ms