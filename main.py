import operation
import help

while True:
    print("hello my friend -v-v-\n================================")
    print(" press 1 for login \n press 2 for registration \n press 3 to terminate")
    op1 = input()
    if op1 == '2':
        operation.take_user()
        continue
    elif op1 == '1':
        print("==================================login===============================")
        while True:
            password = input("enter yor password ,please\n")
            if operation.login(password):
                while True:
                    help.print_menu()
                    op = input()
                    if op == '1':
                        operation.view_all_project()
                    elif op == '2':
                        while True:
                            id = input("enter id\n")
                            if operation.edit_project(int(id)):
                                break
                    elif op == '3':
                        while True:
                            id = input("enter id\n")
                            if operation.delete_project(int(id)):
                                break
                    elif op == '4':
                        operation.take_project()
                    elif op =='5':
                        help.search()
                        break
                    elif op =='6':
                        break
                    else:
                        print("invalid operation")
                break
    elif op1 == '3':
        break

    else:
        print("invalid operator ^-^")
        continue
