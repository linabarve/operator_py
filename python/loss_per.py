c = int(input("enter the cost price:"))
s = int(input("enter the selling price:"))
if c > s:
    l = c - s
    p = (l*100)/c
    print(p)
else:
    print("invalid")