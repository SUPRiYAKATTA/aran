
b=input("enter number")
def pal(x):
	a=x[::-1]
	return a
x=pal(b)
if (x==b):
	print("palindrome")
else:
	print("not a palindrome")
