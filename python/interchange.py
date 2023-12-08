"""#interchange the value of two variable.........
a = int(input())
b = int(input())
c = a;
a = b;
b = c;
print(a,b)
"""

#interchange the value of two variable without using third variable...
a = int(input("enter the value:"))
b = int(input("enter the value:"))
a,b=b,a;
print(a,b)
