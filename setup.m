currentDir = pwd;
filename = "main.slx";

cd(currentDir);
addpath(genpath(currentDir));

model = strcat(strrep(filename, '.slx', ''),"/");
open_system(model);

try
    matlab.engine.shareEngine;
    disp('MATLAB engine shared successfully.');
catch ME
    disp(['Error sharing MATLAB engine: ', ME.message]);
end