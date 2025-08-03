function new_feedback_state = update_feedback_state(current_feedback_state, requested_feedback_state)
    
    expected_state = mod(requested_feedback_state, 3);

    new_feedback_state = current_feedback_state + 1;
    
    while mod(new_feedback_state, 3) ~= expected_state || new_feedback_state == 0
        new_feedback_state = mod(new_feedback_state + 1, 10);
    end
end