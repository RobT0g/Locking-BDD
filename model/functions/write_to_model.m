function write_to_model(var_name, payload, var_type)
model = evalin('base',"model");
level = evalin('base',"level");

    set_param( ...
        strcat(model, var_name), ...
        var_type, ...
        mat2str(payload));

end

