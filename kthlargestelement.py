N=int(input())
K=int(input())
x=K-1
a=[]
for i in range(N):
	b=int(input())
	a.append(b)
a.sort()
c=a[::-1]
print(c[x])
