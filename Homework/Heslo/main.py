import re

while True:

    try:
        username = input("Enter your Username: ")



    except ValueError:
        print("Try again")
    else:
        break

while True:
    try:
        password = input("Enter your Password: ")

    except ValueError:
        print("Try again")
    else:
        break


def password_policy_check(username, password):
    if len(password) < 10 or password == "" or not re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-])", password):
        return False
    # if len(password) < 10 or password == "" or re.search("[\',!;\?\$\^:\\\/`\|~&\" @#%\*\{}\(\)_\+\.\s=-]", password) or re.search(username, password) or not re.search(("[A-Z]+[0-9]+[a-z]+"),password):

    else:
        for i in range(4, len(username)):
            if username[:i] in password:
                return False
    return True
print(password_policy_check(username, password))