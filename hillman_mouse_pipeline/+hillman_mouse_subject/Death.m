
%{
# death
-> hillman_mouse_subject.Subject                 
---
dod: date                      # mouse date of death
reason_of_death: enum('sack','perfusion','terminal','other')
death_notes='': varchar(255)
death_ts = CURRENT_TIMESTAMP: timestamp
%} 

classdef Death < dj.Manual
  
end

