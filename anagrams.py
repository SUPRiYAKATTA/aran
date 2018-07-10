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
    for i in arr:
        x=arr.count(i)
        new.append(x)
    print(max(new))
if __name__ == '__main__':
	main()
