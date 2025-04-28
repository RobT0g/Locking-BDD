function [payload] = read_from_model(var_name)
model = evalin('base',"model");
level = evalin('base',"level");

payload = get_param( ...
    strcat(model,level,var_name), ...
    "RuntimeObject" ).InputPort(1).Data;

end
