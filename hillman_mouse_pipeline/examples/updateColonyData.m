function updateColonyData

% Those are the steps needed to insert the colony data into the database:
% 1. Load all subjects from the colony spreadsheet
% 2. Check which subject is not in the database
% 3. Check for mistakes\typos in the subjects that are going to be inserted
%   to the database
% 4. Check if there are subjects in the database that need to be updated
%   based on update in the colony spreadsheet (TBD)
% 5. Assign the attributes for the subjects need to be inserted.
% 6. Insert the data into the database
% 7. update the subjects that need to be updated.
% Those steps are based on my understanding of the lab workflow.Please revisit and adjust it to your needs 

subject_yaki_matlab.configSchema;
% parameters
numOfVariableInTable = 8;

% load data from colony spreadsheet:
colonyTable = readtable(colonyFileName);
% locate the strain table
lineNameInd = find(strcmp(colonyTable.Properties.VariableNames,lineName));
colonyStrain_tmp = colonyTable(:,lineNameInd:numOfVariableInTable);
colonyStrainT = cell2table(colonyStrain_tmp{2:end,:});
colonyStrainT.Properties.VariableNames = colonyStrain_tmp{1,:};
nullRow = strfind(colonyStrainT.ID,'');
a = colonyStrainT.ID{4}; 

%colonySubjectList_spreadsheet = colonyTable.(lineName)(2:end);

% load data from database:
%colonySubjectList_db = fetch(subject_yaki_matlab.SubjectYakiMatlab ...
%                          * subject_yaki_matlab.Zigosity...
%                          & 'alleleName' = lineMame ...
%                         ,'subject_colony_name');
colonySubjectList_db = fetch(subject_yaki_matlab.SubjectYakiMatlab,'subject_id');
% the spreadsheet contains empty rows
colonySubjectList_db = [{colonySubjectList_db.subject_id},{''}];
% locate the new subjects

newSubjects = setdiff(colonyStrainT.ID,colonySubjectList_db);
colonyStrainT.Properties.RowNames = colonyStrainT.ID;
%newSubjects = setdiff(colonySubjectList_spreadsheet,colonySubjectList_db);

for iSubj=1:length(newSubjects)
    currentSubj = newSubjects{iSubj};
    % tests if the data in the seardsheet is valid
    
    % insert data into structure:
    
    data = struct(...
        'subject_id',currentSubj, ...
        'subject_nickname','', ...
        'subject_colony_name','', ... 
        'dob','', ...
        'sex','', ...
        'breeding_pair','', ...
        'subject_type','', ...
        'mark','', ... 
        'source_name','', ...
        'strain_name','' ...             
    );
    %insert data into the database
    insert(subject_yaki_matlab.SubjectYakiMatlab,data);
end



