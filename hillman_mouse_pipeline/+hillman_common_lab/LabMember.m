%{
  user        : varchar(32)
  ---
  full_name  : varchar(32) 
  -> Lab
%}

classdef LabMember < dj.Lookup
    properties
        contents = {{'richardyan', 'hillmanlab'}, {'wenzeli', 'hillmanlab'}} % need an update
    end
end
