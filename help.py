import  operation


def print_menu():
    print("\t\t===============main===================")
    print("\t\t\t\tpress 1 to view all project")
    print("\t\t\t\tpress 2 to edit")
    print("\t\t\t\tpress 3 to delete")
    print("\t\t\t\tpress 4 to add project")
    print("\t\t\t\tpress 5 to search")
    print("\t\t\t\tpress 6 to exit")


def search():
    print("\t\t\t\tpress 1 to search use id")
    print("\t\t\t\tpress 2 to search use title")
    print("\t\t\t\tpress 3 to to search use start date")
    print("\t\t\t\tpress 4 to to search use last date")
    op = input()
    if op == '1':
        id1 = input("enter id \n")
        found, element, index = operation.search('ID',int(id1))
        if found:
            operation.print_project(element)
    elif op == '2':
        id1 = input("enter title \n")
        found, element, index = operation.search('title',id1)
        if found:
            operation.print_project(element)
    elif op == '3':
        id1 = input("enter start date \n")
        found, element, index = operation.search('start_date',id1)
        if found:
            operation.print_project(element)
    elif op == '4':
        id1 = input("enter end date \n")
        found, element, index = operation.search('end_date',id1)
        if found:
            operation.print_project(element)

    else:
        print("not valid choice 6_6")


