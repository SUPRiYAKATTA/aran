def main():
    a=input()
    b=0
    stack=[]
    for i in range(len(a)):
        if a[i]=="(":
            stack.append(a[i])
        elif a[i]==")":
            if len(stack)>0:
                stack.pop()
            else:
                b=1

    if (len(stack)==0):
        if(b==1):
            print("not balanced")
        else:
            print("balanced")
    else:
        print("not balanced")
        
if __name__ == '__main__':
    main()
