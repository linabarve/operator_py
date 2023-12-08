# electricity bill 
u = int(input("Enter the units: "))
if u <= 100:
    print("No Charge")
elif u <= 200:
    c = (u - 100) * 5
    print("Charge:", c)
elif u >= 400:
    c = (u - 200) * 10
    print("Charge:", c)
else:
    print("Invalid input")

