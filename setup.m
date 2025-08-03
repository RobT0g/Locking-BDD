currentDir = pwd;
cd(currentDir);
addpath(genpath(currentDir));

model = "feature_model";
open_system(strcat(model, "/"));

matlab.engine.shareEngine;