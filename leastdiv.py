def main():
    a_arr=[]
    b_arr=[]
    c_arr=[]
    a=int(input())
    b=int(input())
    if (a==0 or b==0):
        print("Enter valid input")
    else:
        for i in range(1,10000):
            value=a*i
            a_arr.append(value)
        for i in range(1,10000):
            value_1=b*i
            b_arr.append(value_1)
        for i in range(len(a_arr)):
            if a_arr[i] in b_arr:
                c_arr.append(a_arr[i])
        print(c_arr[0])


if __name__ == '__main__':
    main()
