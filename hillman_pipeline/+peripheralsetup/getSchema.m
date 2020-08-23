function obj = getSchema
persistent schemaObject
if isempty(schemaObject)
    schemaObject = dj.Schema(dj.conn, 'peripheralsetup', 'hillman_peripheralsetup');
end
obj = schemaObject;
end
