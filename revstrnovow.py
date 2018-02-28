    a=str(input())
    b=a[::-1]
    d=["a","e","o","i","u"]
    c=list(b)
    for i in c:
        if i in d:
            c.remove(i)
    c="".join(c)
    print(c)
