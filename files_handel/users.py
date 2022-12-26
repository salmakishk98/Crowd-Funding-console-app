import time
import math
import json

path = "C:\\Users\salmakishk\OneDrive - Fculty Of Engineering (Tanta University)\Desktop\projectWithJeson\\files\\users.json"

def prepare_user_to_json(information_list):
    information = {}
    labels = ['ID', 'firstName', 'lastName', 'email', 'password', 'mobile']
    index = 1
    information['ID'] = math.ceil(time.time())
    for i in information_list:
        label = labels[index]
        index += 1
        information[label] = i
    return information



def add_user_to_json(information_list):
    with open(path, "r") as file:
        data = json.load(file)
    data.append(prepare_user_to_json(information_list))
    data_to_json = json.dumps(data, indent=6)
    with open(path, "w") as file:
        file.write(data_to_json)


def get_all_user_from_file():
    with open(path, "r") as file:
        data = json.load(file)
    return data


