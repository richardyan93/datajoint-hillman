
%{
# allele
allele_name:    varchar(64)                # unique allele id
---
standard_name: varchar(255)	
(allele_source) -> hillman_common_lab.Source
allele_url='': varchar(255)                   # link to the line information
allele_ts = CURRENT_TIMESTAMP: timestamp
%}

classdef Allele < dj.Lookup
    
end

