s = float(input("enter the selling:"))
c = float(input("enter the cost price:"))
if s > c:
    p = s-c
    k = (p*100)/c
    print(k)
else:
    print("invalid")