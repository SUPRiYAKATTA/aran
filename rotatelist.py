n=int(input())
a=[]
for i in range(n):
    b=int(input())
    a.append(b)
d=int(input())
def left_rotation(a):
    return a[d:]+a[:d]
print("The array:",a)
print("LEFT ROATION",left_rotation(a))
