a=int(input())
    fact=1
    if a<0:
        print("Enter a positive number")
    else:
        for i in range(0,a):
            i=i+1
            fact=fact*i
        print (fact)
