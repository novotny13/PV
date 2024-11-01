
print("Enter your birthdate")
day = 0
month = 0
year = 0
while True:
    try:
        day = int(input("Day: "))
        if day<= 0 or day>31:
            raise Exception("Invalid day")



        month = int(input("Month: "))
        if month<= 0 or month>12:
            raise Exception("Invalid month")



        year = int(input("year: "))
        if year <= 1905 or year > 2024:
            raise Exception("Invalid year")
    except Exception:
        print("Invalid input. Please enter a valid input.")
    except ValueError:
        print("Invalid input. Please enter a valid input.")
    else :
        break
print ("Your birthdate is: "+str(day)+"."+str(month)+"."+str(year))
