function obj = getSchema
persistent schemaObject
if isempty(schemaObject)
    schemaObject = dj.Schema(dj.conn, 'organism', 'hillman_organism');
end
obj = schemaObject;
end
