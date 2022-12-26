import validation
import files_handel

def take_project():
    information =[]
    while True:
        titel = input("enter project title, please\n")
        if len(titel):
            information.append(titel)
            break
        print("invalid title")
    while True:
        details = input("enter project details, please\n")
        if len(details):
            information.append(details)
            break
        print("invalid details")

    while True:
        total_target = input("enter project total target, please\n")
        if len(total_target) and total_target.isdigit():
            information.append(int(total_target))
            break
        print("total target must be number")
    while True:
        start_date = input("enter project start date like 10-02-2001, please\n")
        if validation.validate_date(start_date):
            information.append(start_date)
            break
    while True:
        end_date = input("enter project end date like 10-02-2001, please\n")
        if validation.validate_date(end_date) and validation.compare_date(information[3],end_date):
            information.append(end_date)
            break
    files_handel.add_project_to_json(information)
    print("project is add successfully ^-^")


def print_project(project):
    print("="*100)
    print(f"project ID is {project['ID']}")
    print("=" * 100)
    print(f"project title is {project['title']}")
    print("=" * 100)
    print(f"details are {project['details']}")
    print("=" * 100)
    print(f"total target is {project['total_target']}")
    print("=" * 100)
    print(f"project begins from  {project['start_date']} and end on {project['end_date']}")
    print("=" * 100)


def view_all_project():
    data = files_handel.get_all_project_from_file()
    for i in data:
        print_project(i)

def search(key, element):
    data = files_handel.get_all_project_from_file()
    for index, i in enumerate(data):
        if i[key] == element:
            return True, i, index
    return False, {}, -1


def delete_project(ID):
    data = files_handel.get_all_project_from_file()
    found, element, index = search("ID",ID)
    if found:
        del data[index]
        files_handel.add_all_project_to_file(data)
        print("project is deleted successfully ^-^")
        return True
    return False

def edit_project(ID):
    try:
        delete_project(ID)
    except:
        print("project not found")
        return False
    print("add new project")
    take_project()
    return True



