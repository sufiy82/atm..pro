L1=[1,2,3,1,1,2,3,2,2]
n=int(input("Enter element to find"))
c=0
for i in range (0,len(L1),1):
    if(L1[i]==n):
        c=c+1
print("The count of element in list",c)
