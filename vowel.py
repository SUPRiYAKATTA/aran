 s=input()
    if s.isnumeric():
        print("enter valid alphabet")
    else:
        if(s=='a' or s=='A'or s=='e' or s=='E' or s=='I' or s=='i' or s=='o' or s=='O' or s=='u' or s=='U'):
            print("vowel")
        else:
            print("consonant")
