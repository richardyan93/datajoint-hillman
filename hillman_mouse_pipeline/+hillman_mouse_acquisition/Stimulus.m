%{
-> hillman_mouse_acquisition.CameraRun
---
stim_type             : enum('air puff', 'whisker', 'visual')
stim_duration         : float
stim_number           : tinyint unsigned
stim_randomized       : boolean
frame_rate            : decimal(8, 4)
%}

classdef Stimulus < dj.Manual
end