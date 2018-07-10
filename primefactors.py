def main():
    import math
    a=int(input())
    b=[]
    c=[]
    for x in range(2,a):
        if(a%x)==0:
            b.append(x)
    def prime(n):
        if n == 2:
            c.append(str(n))
        if n % 2 == 0 or n <= 1:
            return False
        sqr = int(math.sqrt(n)) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        c.append(str(n))
    if prime(a)==a:
        print(a)
    else:
        for n in b:
            prime(n)
        print(' '.join(c))
if __name__ == '__main__':
    main()
