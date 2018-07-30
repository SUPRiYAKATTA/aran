N=int(input())
a=[]
for i in range(N):
	x=int(input())
	a.append(x)
b=sorted(a)
c=b[::-1]
print(b[0],c[0])
	
