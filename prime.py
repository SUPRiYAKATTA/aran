num=100
num=int(raw_input())
if num > 1:
        for i in range(2,num):
         if (num % i)==0:
           print (num,"the number is composite")
           break
         else:
           print(num,"the number is prime")
           break
elif(num==1):
	print "neither prime nor composite"
else:
	print "enter a valid number"
