%{
-> hillman_mouse_acquisition.Session
run_index  : varchar(3)    # e.g. A, B, C.., ZA 
---
run_type              : enum('resting state', 'passive stimulus', 'behavior')
led_number            : tinyint unsigned
run_duration          : float
%}

classdef CameraRun < dj.Manual
    
end

