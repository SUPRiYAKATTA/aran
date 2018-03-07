x=int(input())
list=[]
list2=[]
s=[]
for i in range(x):
    a=input()
    list.append(a)
print(list)
for i in list:
    if list.count(i)>1:
        print(i)
        list2.append(i)
list2.sort()
for i in list2:
    if i not in s:
        s.append(i)
print(s)
