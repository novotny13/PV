

name = input("Hello, what is your name?")
Sure = input("Are you sure your name is :" + name + "?")

while Sure == "no":
    name = input("Hello, what is your name?")
    Sure = input("Are you sure your name is :" + name + "?")

print("good bye")