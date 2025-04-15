from behave import *

@given('the door {door_id} is {door_state}')
def step_given_the_door_is_in_state(context:any, door_id:str, door_state:str):
    pass

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

