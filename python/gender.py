# accept the age gender m,f,and the number of days......		
a = int(input("Enter the age: "))
g = input("Enter gender (m/f): ")
d = int(input("Enter the number of days worked: "))

if a >= 18 and a <= 40:
    if g == "m":
        w = d * 700
    elif g == "f":
        w = d * 750
    else:
        print("Invalid gender input.")
    
    print(w)
    
    if a >= 30 and a <= 40:
        if g == "m":
            w = d * 800
        elif g == "f":
            w = d * 850
        else:
            print("Invalid gender input.")
        
        print(w)
else:
    print("Age is not within the valid range (18-40).")

