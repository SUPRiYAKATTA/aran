from numpy import median
n=5
d=4
p=n-d
ex=[1,2,3,4,4]
notification=0
for i in range(p):
    fp=sorted(ex[i:d])
    fq=ex[d]
    d+=1
    if fq>=2*median(fp):
        notification+=1
print(notification)
