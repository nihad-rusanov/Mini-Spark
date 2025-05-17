import csv

def read_csv(filepath):
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

import json

def read_json(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

def write_to_file(filepath, data):
    with open(filepath, 'w') as f:
        for item in data:
            f.write(str(item) + '\n')
