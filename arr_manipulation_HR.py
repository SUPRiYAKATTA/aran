def main():
    arr=[]
    n=int(input())
    m=int(input())
    for i in range(n):
        arr.append(0)
    for i in range(m):
        a=int(input())
        b=int(input())
        x=int(input())
        start_index=min(n,a)
        stop_index=min(n,b)
        for index in range(start_index-1,stop_index):
            arr[index] += x
        print(arr)
    print(max(arr))
if __name__ == '__main__':
    main()
