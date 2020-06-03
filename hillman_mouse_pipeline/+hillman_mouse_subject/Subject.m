
%{
# Subject
subject_id: varchar(32)                  # unique mouse id
---
subject_colony_name: varchar(255)
dob: date                     # mouse date of birth
sex: enum('M', 'F', 'U')       # sex of mouse - Male, Female, or Unknown/Unclassified
breeding_pair='':    varchar(255)             # 2 str for parents
-> hillman_mouse_subject.Species
mark_type: enum('ear', 'toe', 'tail')
mark='':             varchar(128) 
-> hillman_common_lab.Source
-> hillman_mouse_subject.Strain                              
subject_notes='':    varchar(1024)s
subject_ts = CURRENT_TIMESTAMP: timestamp
%}

classdef Subject < dj.Manual
  
end

