from behave import *
from features.environment import ModelManager
import time

def get_all_doors_locking_state(context) -> list[int]:
    """
    Returns the state of all doors as a list.
    """
    return [int(context.model.read_from_model(f'door_lock_state_{i}')) for i in range(1, 5)]

def get_all_doors_release_state(context) -> list[int]:
    """
    Returns the release state of all doors as a list.
    """
    return [int(context.model.read_from_model(f'door_release_state_{i}')) for i in range(1, 5)]

@given('all doors are {state}')
def step_given_all_doors_are_in_state(context:any, state:str):
    state = state.replace("'", "").replace('"', '')

    if state == 'open':
        for i in range(1, 5):
            context.model.write_to_model(f'door_open_{i}', 1)
        
        return

    elif state == 'closed':
        for i in range(1, 5):
            context.model.write_to_model(f'door_open_{i}', 0)

        return

    elif state == 'locked':
        context.model.write_to_model(f'manual_lock', 15)

    elif state == 'unlocked':
        context.model.write_to_model(f'manual_lock', 0)

    else:
        raise ValueError('state must be either locked or unlocked')

    context.model.write_to_model('manual_lock_rqst', 0)
    time.sleep(0.2)
    context.model.write_to_model('manual_lock_rqst', 1)
    time.sleep(0.2)
    context.model.write_to_model('manual_lock_rqst', 0)

    step_then_all_doors_should_be(context, state)

@given("my vehicle is {state} with no release buttons pressed")
def step_given_my_vehicle_is_in_state(context:any, state:str):
    step_given_all_doors_are_in_state(context, state)

    for i in range(4):
        context.model.write_to_model(f'door_release_{i+1}', 0)

def set_door_lock_model(context:any, door_id:int, expected_state:int):
    current_state = get_all_doors_locking_state(context)

    if expected_state == 'locked':
        current_state[door_id] = 1

    elif expected_state == 'unlocked':
        current_state[door_id] = 0

    else:
        raise ValueError('door_state must be either locked or unlocked')

    set_state = 0
    for i in range(4):
        if current_state[i] == 1:
            set_state += 2**i

    context.model.write_to_model(f'manual_lock', set_state)

    context.model.write_to_model('manual_lock_rqst', 0)
    time.sleep(0.2)
    context.model.write_to_model('manual_lock_rqst', 1)
    time.sleep(0.2)
    context.model.write_to_model('manual_lock_rqst', 0)

    assert get_all_doors_locking_state(context)[door_id] == current_state[door_id], f'Failed to set the door {door_id} to {expected_state}. Expected {current_state[door_id]}, got {get_all_doors_locking_state(context)[door_id]}'

def set_door_release_model(context:any, door_id:int, expected_state:int):
    if expected_state == 'open':
        context.model.write_to_model(f'door_open_{door_id+1}', 1)

    elif expected_state == 'closed':
        context.model.write_to_model(f'door_open_{door_id+1}', 0)
    
    else:
        raise ValueError('door_state must be either open or closed')

@given('the door {door_id} is {expected_state}')
def step_given_the_door_is_in_state(context:any, door_id:str, expected_state:str):
    door_id = int(door_id.replace("'", "").replace('"', ''))-1
    expected_state = expected_state.replace("'", "").replace('"', '')

    if door_id < 0 or door_id > 3:
        raise ValueError('door_id must be between 1 and 4')

    if expected_state in ['locked', 'unlocked']:
        set_door_lock_model(context, door_id, expected_state)
    
    elif expected_state in ['open', 'closed']:
        set_door_release_model(context, door_id, expected_state)

    else:
        raise ValueError('expected_state must be either locked, unlocked, open or closed')

@given('I {key_present} an authenticated key with me')
def step_given_i_have_an_authenticated_key_with_me(context:any, key_present:str):
    key_status = key_present.replace("'", "").replace('"', '')

    if key_status == 'have':
        context.model.write_to_model('key_detected', 1)
    
    elif key_status == 'do not have':
        context.model.write_to_model('key_detected', 0)
    
    else:
        raise ValueError('key_present must be either have or do not have')

@when('I press the {operation} button')
def step_when_i_press_the_operation_button(context:any, operation:str):
    operation = operation.replace("'", "").replace('"', '')

    if operation not in ['lock', 'unlock']:
        raise ValueError('operation must be either lock or unlock')

    context.model.write_to_model(f'{operation}_all_button', 0)
    time.sleep(0.2)

    context.model.write_to_model(f'{operation}_all_button', 1)
    time.sleep(0.2)

    context.model.write_to_model(f'{operation}_all_button', 0)
    time.sleep(0.2)

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
    step_then_all_doors_should_be(context, state)

@when('I wait {wait_time} {time_unit}')
def step_when_i_wait(context:any, wait_time:str, time_unit:str):
    wait_time = int(wait_time.replace("'", "").replace('"', ''))
    time_unit = time_unit.replace("'", "").replace('"', '')

    if time_unit == 'seconds':
        time.sleep(wait_time)

    elif time_unit == 'milliseconds':
        time.sleep(wait_time / 1000)

    else:
        raise ValueError('time_unit must be either seconds or milliseconds')

@then('all doors should be {state}')
def step_then_all_doors_should_be(context:any, state:str):
    state = state.replace("'", "").replace('"', '')

    door_states = [context.model.read_from_model(f'door_lock_state_{i}') for i in range(1, 5)]

    if state == 'locked':
        assert all(d == 1 for d in door_states), f'Failed to set all doors to {state}'

    elif state == 'unlocked':
        assert all(d == 0 for d in door_states), f'Failed to set all doors to {state}'

    else:
        raise ValueError('state must be either locked or unlocked')

@then('the door {door_id} should be {state}')
def step_then_the_door_should_be(context:any, door_id:str, state:str):
    door_id = int(door_id.replace("'", "").replace('"', ''))-1
    state = state.replace("'", "").replace('"', '')

    if door_id < 0 or door_id > 3:
        raise ValueError('door_id must be between 1 and 4')

    if state in ['locked', 'unlocked']:
        check_door_is_in_lock_state(context, door_id, state)

    elif state in ['held', 'released']:
        check_door_is_in_release_state(context, door_id, state)

    else:
        raise ValueError('state must be either locked, unlocked, held or released')

@then('I should receive a {feedback_type} feedback within {timeout} ms')
def step_then_i_should_receive_feedback(context:any, feedback_type:str, timeout:str):
    feedback_type = feedback_type.replace("'", "").replace('"', '')
    timeout = int(timeout.replace("'", "").replace('"', ''))

    context.model.scenario_feedback_count += 1

    if feedback_type == 'locking confirmation':
        feedback_type = 1

    elif feedback_type == 'unlocking confirmation':
        feedback_type = 2

    elif feedback_type == 'locking failed':
        feedback_type = 0
    
    else:
        assert False, f'Unknown feedback type: {feedback_type}'

    start_time = context.model.get_elapsed_time_ms()
    condition_met = False

    while (context.model.get_elapsed_time_ms() - start_time) < timeout:
        if context.model.scenario_feedback_transitions[-1] == feedback_type:
            condition_met = True
            break

        time.sleep(0.05)
        context.model.update_model_time()
        context.model.update_feedback()

    assert context.model.scenario_feedback_count == len(context.model.scenario_feedback_transitions), \
        f'Feedback count mismatch: expected {context.model.scenario_feedback_count}, got {len(context.model.scenario_feedback_transitions)}'
    assert condition_met, f'Expected feedback "{feedback_type}" not received within {timeout} ms. Last received feedback: "{context.model.last_feedback}"'

def check_door_is_in_lock_state(context:any, door_id:int, expected_state:str):
    current_state = get_all_doors_locking_state(context)

    if expected_state == 'locked':
        assert current_state[door_id] == 1, f'Failed to set the door {door_id} to {expected_state}. Expected {current_state[door_id]}, got {get_all_doors_locking_state(context)[door_id]}'

    elif expected_state == 'unlocked':
        assert current_state[door_id] == 0, f'Failed to set the door {door_id} to {expected_state}. Expected {current_state[door_id]}, got {get_all_doors_locking_state(context)[door_id]}'

    else:
        raise ValueError('expected_state must be either locked or unlocked')

def check_door_is_in_release_state(context:any, door_id:int, expected_state:str):
    current_state = get_all_doors_release_state(context)

    if expected_state == 'held':
        assert current_state[door_id] == 0, f'Failed to set the door {door_id} to {expected_state}. Expected {current_state[door_id]}, got {current_state}'

    elif expected_state == 'released':
        assert current_state[door_id] == 1, f'Failed to set the door {door_id} to {expected_state}. Expected {current_state[door_id]}, got {current_state}'

    else:
        raise ValueError('expected_state must be either held or released')
