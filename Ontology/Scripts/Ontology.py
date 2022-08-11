import os

## returns a list of model IDs that are strings in the form of Parent:Child:Grandchild
def get_ontology(directory):
    r = []
    dirpath, dirnames, filenames = next(os.walk(directory))
    dirpath = dirpath.replace(".\\", "").replace("\\", ":")
    for dir in dirnames:
        r.append(dirpath + ":" + dir)
    for name in filenames:
        r.append(dirpath + ":" + name.split(".json")[0])
    return r


print(get_ontology(".\Ontology\Willow"))
