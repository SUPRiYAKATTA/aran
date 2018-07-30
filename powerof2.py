def p2(n):
	if n==0:
		return "yes"
	while(n!=1):
		if((n%2!=0)):
			return "no"
		n=n//2
	return "yes"
n=int(input())
print(p2(n))
