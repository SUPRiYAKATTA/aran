a=[]
    n=int(input())
    for i in range(0,n):
        b=int(input("enter elements:"))
        a.append(b)
    a.sort()
    print(a)
    print("largest element",a[n-1])
