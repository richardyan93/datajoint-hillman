%{
-> hillman_mouse_subject.Subject
session_date      : date
session_index     : tinyint unsigned
---
(session_location) -> hillman_mouse_lab.Location
(primary_experimenter) -> hillman_mouse_lab.User
data_directory    : varchar(128)
%}

classdef Session < dj.Manual
    
end

