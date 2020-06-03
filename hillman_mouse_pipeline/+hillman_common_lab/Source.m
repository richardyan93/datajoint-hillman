
%{
source_name:    varchar(32)               # unique source id
---
source_full_name='': varchar(255)  				  # name of source
contact_details='': varchar(255)              
link_to_wedsite='':  varchar(255)            
source_description='':	varchar(255)  
source_ts = CURRENT_TIMESTAMP: timestamp
%}

classdef Source < dj.Lookup
    
end

