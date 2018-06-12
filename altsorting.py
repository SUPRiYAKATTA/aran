def main():
    a=int(input())
    arr=[]
    for i in range(a):
        b=int(input())
        arr.append(b)
    arr.sort()
    c=arr[::-1]
    newarray = sum(zip(c,arr),())[:len(arr)]
    print( "".join( repr(e) for e in  newarray) )



if __name__ == '__main__':
    main()
