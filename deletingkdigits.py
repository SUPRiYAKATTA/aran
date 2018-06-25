def main():
    n=input()
    k=input()
    if(k.isalpha()):
        print("enter valid 'k' value")
    else:
        c=int(k)
        if(c<=len(n)):
            print(n[c:])
        else:
            print("enter valid 'k' value")



if __name__ == '__main__':
    main()
