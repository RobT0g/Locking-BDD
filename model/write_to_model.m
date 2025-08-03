function write_to_model(var_name, payload, var_type)
%model = evalin('base',"model");

set_param( ...
    var_name, ...
    var_type, ...
    mat2str(payload));

end

