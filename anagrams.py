def main():
    a=[]
    arr=[]
    count=0
    n=int(input())
    for i in range(n):
        b=input()
        a.append(b)
    for i in range(len(a)):
        b=''.join(sorted(a[i]))
        arr.append(b)
    for i in range(len(arr)):
        if arr[i]==arr[i-1]:
            count=count+1
    print(count)
if __name__ == '__main__':
    main()
