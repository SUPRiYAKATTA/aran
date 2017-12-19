 a=input()
    b=input()
    c=input()
    if (a.isnumeric() and b.isnumeric() and c.isnumeric()):
        if (a>b and a>c):
            print(a)
        if (b>c and b>a):
            print (b)
        if (c>a and c>b):
            print(c)
        else:
            print("all are equal")
    else:
        print ("enter valid number")
