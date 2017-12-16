list=[]
nterms=100
nterms=int(input('enter the no of terms'))
n1=0
n2=1
list.append(n1)
list.append(n2)
count=0
print(nterms)
if nterms==1:
   print('the fibonacci series upto',nterms,":")
   print(n1)
   list.append(n1)
else:
    print('the fibonacci series upto',nterms,":")
    while count<nterms:
    	print(n1)
    	nxt=n1+n2
    	n1=n2
    	n2=nxt
    	count+=1
    	list.append(nxt)
print list
