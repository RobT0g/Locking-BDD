# In order to access my vehicle, as a vehicle owner, I want to unlock a single door by interacting with it while my key is with me 

Feature: Unlock individual door
    Scenario Outline: Unlocking a single door when I have the key
        Given the door <door_id> is 'locked'
        And I have an authenticated key with me
        
        When I press the door <door_id> release button
        
        Then the door <door_id> should be 'unlocked'
        And the door <door_id> should be 'released'

        Examples:
            | door_id |
            | 1       |
            | 2       |
            | 3       |
            | 4       |

    Scenario Outline: Individual door is left unlocked
        Given the door <door_id> is 'locked'
        And I have an authenticated key with me
        
        When I press the door <door_id> unlock button
        And I wait '1' seconds
        And I release the door <door_id> release button
        
        Then the door <door_id> should be 'unlocked'
        And the door <door_id> should be 'held'

        Examples:
            | door_id |
            | 1       |
            | 2       |
            | 3       |
            | 4       |
