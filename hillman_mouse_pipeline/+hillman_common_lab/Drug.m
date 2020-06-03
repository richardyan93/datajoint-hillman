%{
# Drug
drug    : varchar(32)
---
(drug_source) -> hillman_lab.Source
drug_description='': varchar(255)
%}

classdef Drug < dj.Lookup
    properties
        contents = {{'caffeine'}, {'alcohol'}} % need an update
    end
end
