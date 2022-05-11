import pickle
import json
import yaml

def to_pickle(obj, file): # Сериализация по PICKLE
    file_1 = open(file,"wb")
    output = pickle.dump(obj, file_1,pickle.HIGHEST_PROTOCOL)
    return output

def to_json(obj, file): # Сериализация по JSON
    with open(file, "wt") as f:
        json.dump(obj, f, indent=4)

def to_yaml(obj, file): # Сериализация по YAML
    with open(file, "wt") as f:
        yaml.dump(obj, f)

def from_pickle(file):
    with open(file, "rb") as f:
        obj = pickle.load(f)
    return obj

def from_json(file):
    with open(file, "rt") as f:
        obj = json.load(f)
    return obj

def from_yaml(file):
    with open(file, "rt") as f:
        obj = yaml.load(f)
    return obj