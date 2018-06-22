def main():
    a=[]
    n=int(input())
    for i in range(n):
        b=int(input())
        a.append(b)
    for i in range(len(a)):
        print(a.pop())
if __name__ == '__main__':
    main()
