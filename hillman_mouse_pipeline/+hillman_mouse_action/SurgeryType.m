%{
# SurgeryType
surgery_type: varchar(32)  # e.g. Craniotomy, Thin-skull, Injection
---
surgery_description: varchar(1024)
%}

classdef SurgeryType < dj.Lookup
    
end