import pickle
import json
import yaml
from yaml.loader import SafeLoader

def from_pickle(file): # Десериализация по PICKLE
    with open(file, "rb") as f:
        obj = pickle.load(f)
    return obj

def from_json(file): # Десериализация по JSON
    with open(file, "rt") as f:
        obj = json.load(f)
    return obj

def from_yaml(file): # Десериализация по YAML
    with open(file, "rt") as f:
        obj = yaml.load(f,Loader=SafeLoader)
    return obj
