%{
  project                     : varchar(32)
  ---
  -> LabMember
  project_description=''      : varchar(1024)
%}

classdef Project < dj.Lookup

end
