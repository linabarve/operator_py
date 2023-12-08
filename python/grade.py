p,c,b,m,c = map(int,input().split())
t = p+c+b+m+c
k = t/500*100
if k >= 90:
	print("Grade A")
elif k >= 80:
	print("Grade B")
elif k >= 70:
	print("Grade c")
elif k >= 60:
	print("Grade D")
elif k >= 40:
	print("Grade E")
else:
	print("Grade F")
