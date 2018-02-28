a=input()
b=0
x=list(map(int,str(a)))
for i in range(0,len(x)):
sq=x[i]*x[i]
        b=sq+b
    print(b)
