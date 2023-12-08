# input basic salary  of an employee and calculate gross salary.....
b = int(input("Enter the basic salary: "))
if b <= 10000:
    HRA = 0.2
    DA = 0.8 
    GS = b + HRA + DA
    print("Gross Salary:", GS)
elif b <= 20000:
    HRA = 0.25
    DA = 0.9
    GS = b + HRA + DA
    print("Gross Salary:", GS)
elif b > 20000:
    HRA = 0.3
    DA = 0.95
    GS = b + HRA + DA
    print("Gross Salary:", GS)

