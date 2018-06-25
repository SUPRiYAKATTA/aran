def main():
    import os
    x=[]
    n=int(input())
    for i in range(n):
        a=input()
        x.append(a)
    print(os.path.commonprefix(x))

if __name__ == '__main__':
    main()
