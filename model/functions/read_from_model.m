function [payload] = read_from_model(var_name)
model = evalin('base',"model");

payload = get_param( ...
    strcat(model,var_name), ...
    "RuntimeObject" ).InputPort(1).Data;

end
