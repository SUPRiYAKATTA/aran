b=int(input())
    fact=1
    if b<0:
        print("Enter a positive number")
    else:
        for i in range(0,b):
            i=i+1
            fact=fact*i
        print (fact)
