n=input("enter the number")
if (n.isnumeric()):
	n=int(n)
	if (n<0):
		print("the number is negative")
	elif (n==0):
		print("the number is 0")
	else:
		print("the number is positive")
else:
	print("invalid input")
