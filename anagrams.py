def main():
    a=[]
    arr=[]
    new=[]
    count=0
    n=int(input())
    for i in range(n):
        b=input()
        a.append(b)
    for i in range(len(a)):
        b=''.join(sorted(a[i]))
        arr.append(b)
    if n==1:
        print(1)
    else:
        for i in arr:
            x=arr.count(i)
            if x==1:
                new.append(0)
            else:
            	new.append(x)
        print(max(new))
if __name__ == '__main__':
    main()
