import time
import math
import json

path = "C:\\Users\salmakishk\OneDrive - Fculty Of Engineering (Tanta University)\Desktop\projectWithJeson\\files\projects.json"

def prepare_project_to_json(information_list):
    information = {}
    labels = ['ID', 'title', 'details', 'total_target', 'start_date', 'end_date']
    index = 1
    information['ID'] = math.ceil(time.time())
    for i in information_list:
        label = labels[index]
        index += 1
        information[label] = i
    return information



def add_project_to_json(information_list):
    with open(path, "r") as file:
        data = json.load(file)
    data.append(prepare_project_to_json(information_list))
    data_to_json = json.dumps(data, indent=6)
    with open(path, "w") as file:
        file.write(data_to_json)


def get_all_project_from_file():
    with open(path, "r") as file:
        data = json.load(file)
    return data

def add_all_project_to_file(allproject):
    data_to_json = json.dumps(allproject, indent=6)
    with open(path, "w") as file:
        file.write(data_to_json)


