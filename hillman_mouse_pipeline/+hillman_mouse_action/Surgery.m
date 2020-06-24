%{
#surgery
-> hillman_mouse_subject.Nickname
surgery_index: tinyint              # it is just for the animal not general.
---
-> hillman_mouse_action.SurgeryType
head_plate: enum('wfom','2P')       # head plate for a specific setup
surgery_date: date                  #       
terminal: bool                      # TBD
-> hillman_mouse_action.Anesthesia
surgery_notes='': varchar(1024)
surgery_ts = CURRENT_TIMESTAMP: timestamp
%}

classdef Surgery < dj.Manual
    
end
