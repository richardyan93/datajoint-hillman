%{
-> hillman_mouse_subject.Subject
session_date      : date
session_index     : tinyint unsigned
---
session_start_time: time
(session_location) -> hillman_mouse_lab.Location
(primary_experimenter) -> hillman_mouse_lab.User
data_directory    : varchar(255)
-> hillman_mouse_action.Anesthesia
-> hillman_mouse_action.Dosage
%}

classdef Session < dj.Manual
    
end

