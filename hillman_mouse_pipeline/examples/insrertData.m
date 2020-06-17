% insertData

%draw(dj.ERD(subject_yaki_matlab.getSchema)) % show the pipeline
%describe(subject_yaki_matlab.Strain) % describe the table
%syncDef(subject_yaki_matlab.Strain)    %update a table

%{
data = struct('strain_name','aas','strain_description','da');
insert(subject_yaki_matlab.Strain,data);
data = struct('strain_name','cw','strain_description','d');
insert(subject_yaki_matlab.Strain,data);

subject_yaki_matlab.Strain

%del(subject_yaki_matlab.Strain & "strain_name='cw'")


data = struct('source_name','1');
insert(subject_yaki_matlab.Source,data);
data = struct('source_name','2');
insert(subject_yaki_matlab.Source,data);

subject_yaki_matlab.Source
%}

data = struct(...
        'subject_id','noOne2', ...
        'subject_nickname','', ...
        'subject_colony_name','', ... 
        'dob','2020-05-22', ...
        'sex','F', ...
        'breeding_pair','A5', ...
        'subject_type','mouse', ...
        'mark','ear', ... 
        'source_name','1', ...
        'strain_name','aas' ...             
    );
insert(subject_yaki_matlab.SubjectYakiMatlab,data);
%data = struct();
%insert(subject_yaki_matlab.SubjectYakiMatlab,data);

subject_yaki_matlab.SubjectYakiMatlab
