"""# Total marks obtained by a student
h,m,e,s,c = map(int,input().split())
T = h+m+e+s+c;
print(T)
"""

h = int(input())
m = int(input())
e = int(input())
s = int(input())
c = int(input())
T = h+m+e+s+c;
per = T/500*100;
print(per)

