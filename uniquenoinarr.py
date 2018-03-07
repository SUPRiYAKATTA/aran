x=int(input())
list=[]
for i in range(x):
        a=input()
        list.append(a)
print(list)
for i in list:
        if list.count(i)==1:
                print(i)
