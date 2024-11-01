print("Enter your birthdate")
day = 0
while 0>= day or day > 31 :
    try:
        day = int(input("Day: "))
    except ValueError:
        print("Invalid input. Please enter a valid input.")
month = 0
while 0>= month or month > 12 :
    try:
        month = int(input("Month: "))
    except ValueError:
        print("Invalid input. Please enter a valid input.")
year =0
while 0>= year or year > 2024 :
    try:
            year = int(input("year: "))
    except ValueError:
            print("Invalid input. Please enter a valid input.")
print ("Your birthdate is: "+str(day)+"."+str(month)+"."+str(year))