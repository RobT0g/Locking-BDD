from behave import *
from features.environment import ModelManager
import time

@given("my vehicle {state} with no release buttons pressed")
def step_given_all_door_are_in_state(context:any, state:str):
    state = state.replace("'", "").replace('"', '')

    for i in range(4):
        context.model.write_to_model(f'door_release_{i+1}', 0)

    assert int(context.model.read_from_model(f'doors_release_state')) == 0, f'Failed to set all doors release buttons to 0'

    if state == 'locked':
        context.model.write_to_model(f'general_locking_manager/set_state_value', 15)

    elif state == 'unlocked':
        context.model.write_to_model(f'general_locking_manager/set_state_value', 0)

    else:
        raise ValueError('state must be either locked or unlocked')

    context.model.write_to_model(f'general_locking_manager/trigger_state_set', 0)
    time.sleep(0.2)
    context.model.write_to_model(f'general_locking_manager/trigger_state_set', 1)
    time.sleep(0.2)
    context.model.write_to_model(f'general_locking_manager/trigger_state_set', 0)

    assert int(context.model.read_from_model('current_door_state')) == (15 if state == 'locked' else 0), f'Failed to set all doors to {state}'

@given('the door {door_id} is {door_state}')
def step_given_the_door_is_in_state(context:any, door_id:str, door_state:str):
    door_id = int(door_id.replace("'", "").replace('"', ''))
    door_state = door_state.replace("'", "").replace('"', '')

    if door_id < 1 or door_id > 4:
        raise ValueError('door_id must be between 1 and 4')

    current_state = context.model.read_from_model('current_door_state')
    assert current_state >= 0 and current_state < 16, 'Failed to get the current_door_state'

    if door_state == 'locked':
        current_state |= 2**(door_id-1)

    elif door_state == 'unlocked':
        current_state &= ~(2**(door_id-1))

    else:
        raise ValueError('door_state must be either locked or unlocked')

    context.model.write_to_model(f'general_locking_manager/set_state_value', current_state)
    context.model.write_to_model(f'general_locking_manager/trigger_state_set', 0)
    time.sleep(0.2)
    context.model.write_to_model(f'general_locking_manager/trigger_state_set', 1)
    time.sleep(0.2)
    context.model.write_to_model(f'general_locking_manager/trigger_state_set', 0)

    assert int(context.model.read_from_model('current_door_state')) == current_state, f'Failed to set the door {door_id} to {door_state}'

@given('I {key_present} an authenticated key with me')
def step_given_i_have_an_authenticated_key_with_me(context:any, key_present:str):
    pass

@when('I press the {operation} button')
def step_when_i_press_the_operation_button(context:any, operation:str):
    step_given_all_door_are_in_state(context, operation+'ed')

@when('I {button_state} the door {door_id} release button')
def step_when_i_press_the_door_release_button(context:any, button_state:str, door_id:str):
    button_state = button_state.replace("'", "").replace('"', '')
    door_id = int(door_id.replace("'", "").replace('"', ''))

    if button_state == 'hold':
        context.model.write_to_model(f'door_release_{door_id}', 1)

    elif button_state == 'release':
        context.model.write_to_model(f'door_release_{door_id}', 0)

    else:
        raise ValueError('button_state must be either press or release')

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
    state = state.replace("'", "").replace('"', '')

    if state == 'locked':
        assert int(context.model.read_from_model('current_door_state')) == 15, f'Failed to set all doors to {state}'

    elif state == 'unlocked':
        assert int(context.model.read_from_model('current_door_state')) == 0, f'Failed to set all doors to {state}'

    else:
        raise ValueError('state must be either locked or unlocked')

@then('the door {door_id} should be {state}')
def step_then_the_door_should_be(context:any, door_id:str, state:str):
    door_id = int(door_id.replace("'", "").replace('"', ''))
    state = state.replace("'", "").replace('"', '')

    if door_id < 1 or door_id > 4:
        raise ValueError('door_id must be between 1 and 4')

    current_state = context.model.read_from_model('doors_release_state')
    assert current_state >= 0 and current_state < 16, 'Failed to get the current_door_state'
    print(f"current_state: {bin(current_state)}, checking if door {door_id} is {state}")

    if state in ['locked', 'released']:
        assert current_state & 2**(door_id-1) == 2**(door_id-1), f'Failed to set the door {door_id} to {state}'

    elif state in ['unlocked', 'held']:
        assert current_state & 2**(door_id-1) == 0, f'Failed to set the door {door_id} to {state}'

    else:
        raise ValueError('state must be either locked, unlocked, held or released')
