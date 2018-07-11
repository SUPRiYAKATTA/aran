def main():
    a=input()
    b=a[::-1]
    c=b.split()
    c.reverse()
    print(" ".join(c))
if __name__ == '__main__':
    main()
