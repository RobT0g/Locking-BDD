from behave import *
from ..environment import ModelManager
import time

@given('the door {door_id} is {door_state}')
def step_given_the_door_is_in_state(context:any, door_id:str, door_state:str):
    if door_id > 4:
        raise ValueError('door_id must be between 1 and 4')

    current_state = context.model.read_from_model('current_door_state')
    assert current_state, 'Failed to get the current_door_state'

    if door_state == 'locked':
        current_state |= 2**(door_id-1)
    
    elif door_state == 'unlocked':
        current_state &= ~(2**(door_id-1))

    else:
        raise ValueError('door_state must be either locked or unlocked')

    context.model.write_to_model(f'general_locking_manager/door_lock_state_memory', door_state)

    assert context.model.read_from_model('current_door_state') == current_state, f'Failed to set the door {door_id} to {door_state}'

@given('I have an authenticated key with me')
def step_given_i_have_an_authenticated_key_with_me(context:any):
    pass

@when('I press the {operation} button')
def step_when_i_press_the_operation_button(context:any, operation:str):
    pass

@when('I {button_state} the door {door_id} release button')
def step_when_i_press_the_door_release_button(context:any, button_state:str, door_id:str):
    pass

@when('all doors get {state}')
def step_when_all_doors_get_state(context:any, state:str):
    pass

@when('I wait {wait_time} {time_unit}')
def step_when_i_wait(context:any, wait_time:str, time_unit:str):
    pass

@when('I turn {vehicle_state} the vehicle')
def step_when_i_turn_the_vehicle(context:any, vehicle_state:str):
    pass

@then('all doors should be {state}')
def step_then_all_doors_should_be(context:any, state:str):
    pass

@then('the door {door_id} should be {state}')
def step_then_the_door_should_be(context:any, door_id:str, state:str):
    pass

