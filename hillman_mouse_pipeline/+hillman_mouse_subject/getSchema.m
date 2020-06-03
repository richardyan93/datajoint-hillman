function obj = getSchema
persistent schemaObject
if isempty(schemaObject)
    schemaObject = dj.Schema(dj.conn, 'subject_yaki_matlab', 'subject_yaki_matlab');
end
obj = schemaObject;
end
