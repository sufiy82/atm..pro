a=0
b=2
n=int(input("enter  number"))
print(a,b)
for i in range(0,n,1):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
