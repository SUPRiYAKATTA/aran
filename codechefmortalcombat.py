T=int(input())
count=0
for i in range(T):
    N=int(input())
    K=int(input())
    a=list(map(int,input().rstrip().split()))
    b=list(map(int,input().rstrip().split()))
c=sorted(a)
d=sorted(b)
for i in range(len(c)):
    for j in range(len(d)):
        if d[j]>c[i]:
            count+=1
if count>=K:
    print("YES")
else:
    print("NO")

