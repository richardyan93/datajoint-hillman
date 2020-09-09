function obj = getSchema
persistent schemaObject
if isempty(schemaObject)
    schemaObject = dj.Schema(dj.conn, 'setup', 'hillman_setup');
end
obj = schemaObject;
end
