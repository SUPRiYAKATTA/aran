def main():
    a=[]
    n=int(input())
    for i in range(0,n):
        b=int(input())
        a.append(b)
    a.sort(reverse=True)
    str1 = ''.join(str(e) for e in a)
    print(str1)




if __name__ == '__main__':
    main()
