%{
# weighing
-> hillman_mouse_subject.Nickname
weighing_time: datetime
---
weight : decimal(4, 1)  # (g)
weight_ts = CURRENT_TIMESTAMP: timestamp
%}

classdef Weighing < dj.Manual
    
end
