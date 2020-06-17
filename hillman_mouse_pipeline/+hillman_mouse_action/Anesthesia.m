%{
#anasthesia
anesthesia:  varchar(32)         # TBD
%}

classdef Anesthesia < dj.Lookup
    
    properties
        contents = {'isoflurane'; 'urethane'; 'ket/xyl'}
    end
    
end