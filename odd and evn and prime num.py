s=[2,5,3,4,7,6,8]
for i in s:
    if(i%2==0):
        print("even number:",i)
    else:
        print("odd number:",i)





        
n=int(input("enter number"))
c=0
print("divisibles of given numbers")
for i in range(2,n,1):
    if(n%i==0):
        print(i)
        c=c+1
if(c==0):
    print(n,"is prime")
else:
    print(n,"is not prime")
