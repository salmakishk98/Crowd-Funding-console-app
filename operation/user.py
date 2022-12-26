import files_handel
import validation


def take_user():
    information = []
    while True:
        name = input("enter your first name, please\n")
        if validation.name_validation(name):
            information.append(name)
            break
    while True:
        name = input("enter your last name, please\n")
        if validation.name_validation(name):
            information.append(name)
            break

    while True:
        email = input("enter your email, please\n")
        if validation.validate_email(email):
            information.append(email)
            break
    while True:
        password = input("enter your password, please\n")
        if validation.password_validation(password):
            information.append(password)
            newpassword = input("conform your password, please\n")
            if validation.check_password(password, newpassword):
                break

    while True:
        mobile = input("enter your mobile, please\n")
        if validation.mobile_validation(mobile):
            information.append(mobile)
            break
    files_handel.add_user_to_json(information)
    print("user is added successfully")



def login(password):
    alluser = files_handel.get_all_user_from_file()
    index = -1
    index = filter(lambda x : x["password"] == password, alluser)
    if index != -1:
        print("the login is done successfuly")
        return True
    print("password not found ^-^")
    return False

