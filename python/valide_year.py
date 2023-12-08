# validate a give year
y = int(input("Enter the year: "))
m = int(input("Enter the month: "))
d = int(input("Enter the day: "))

if y > 0:
    if m >= 1 and m <= 12:
        if d >= 1 and d <= 31:
            print("Valid date")
        else:
            print("Invalid day")
    else:
        print("Invalid month")
else:
    print("Invalid year")

	
