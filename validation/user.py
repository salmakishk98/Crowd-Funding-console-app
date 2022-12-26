import re


def name_validation(name: str):
    if not name.isdigit() and len(name) > 0:
        return True
    print("not valid name")
    return False


def password_validation(password: str):
    numeric = False
    upper = False
    if len(password) < 8:
        print("password must consist of 8 character")
        return False
    for i in password:
        if i.isdigit():
            numeric = True
    if not numeric:
        print("must have numeric")
        return False
    return True


def check_password(oldPassword, newPassword):
    if len(oldPassword) != len(newPassword):
        print("not identical")
        return False
    for i in range(0,len(oldPassword)):
        if(oldPassword[i]!=newPassword[i]):
            print("not identical")
            return False
    return True

def mobile_validation(number):
    if len(number) < 11:
        print("not valid mobile number")
        return False
    if number[0:3] not in ["010","011","015"]:
        print("not valid mobile number")
        return False
    return True

# email must be in form of "user@company.com"
"""
user ----> a-z,A-Z,0-9,_-
company ---->a-zA-Z0-9
com -------> a-z
"""
def validate_email(email):
    true_form = r"[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-z]{1,3}"
    if re.match(true_form,email):
        return True
    print("not valid email")
    return  False


