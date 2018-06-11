def main():
    a=[]
    n=int(input("enter no of elements:"))
    for i in range(0,n):
        b=int(input("enter the elements:"))
        a.append(b)
    a.sort(reverse=True)
    def remove(a):
        final_list=[]
        for num in a:
            if num not in final_list:
                final_list.append(num)
        return final_list
    str1 = ''.join(str(e) for e in remove(a))
    print(str1)




if __name__ == '__main__':
    main()
