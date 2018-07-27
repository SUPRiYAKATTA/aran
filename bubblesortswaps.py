def countSwaps(a):
    count=0
    b=sorted(a)
    while 1:
        flag=True
        for i in range(0,len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                count+=1
                flag=False
        if flag:
            break
    print("Array is sorted in",count,"swaps")
    print("First Element:",a[0])
    print("Last Element:",a[n-1])


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
