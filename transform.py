

def entity_transform(row):
    entity = {}
    if row['party_id']:
        entity["party"] = {}
        entity["party"]["identifier"] = row['party_id']

    return entity