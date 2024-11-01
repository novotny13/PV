import re

while True:

    try:
        nickname = input("Enter your nickname: ")
        while len(nickname) > 100 or nickname == "" or re.search("[\',!;\?\$\^:\\\/`\|~&\" @#%\*\{}\(\)_\+\.\s=-]", nickname):
            print("Your nickname must be less than 100 characters and more then 0 characters")
            print("And you can not use any special characters")
            nickname = input("Enter your nickname: ")


    except ValueError:
        print("Try again")
    else:
        break

while True:
    try:
        phone = input("Enter your message: ")
        while len(phone) > 9 or phone == "" or not re.search("^[0-9]", phone):
            print("Your text must be less than 255 characters and more then 0 characters")
            print("And you can not use any special characters")
            text = input("Enter your message: ")
    except ValueError:
        print("Try again")
    else:
        break


def send_text(nickname, phone):

    sql_update = "UPDATE USER SET  PHONE = {} WHERE USERNAME = '{}'".format(phone, nickname)
    return sql_update
print(send_text(nickname, phone))