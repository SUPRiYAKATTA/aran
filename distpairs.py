def main():
    import math
    two_n=int(input())
    k=2
    x=two_n-k
    ntr= math.factorial(two_n)
    dtr_1=math.factorial(two_n -k)
    dtr_2=math.factorial(k)
    dtr=dtr_1*dtr_2
    dpair=ntr/dtr
    print(dpair)

if __name__ == '__main__':
    main()
