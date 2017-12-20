a=int(input())
    if a<0:
        print("Enter a positive number")
    else:
        for i in range(0,a):
            i=i+1
            b=a*i
            print (a,'*',i,'=',b)
