function obj = getSchema
persistent schemaObject
if isempty(schemaObject)
    schemaObject = dj.Schema(dj.conn, 'experiment', 'hillman_experiment');
end
obj = schemaObject;
end
