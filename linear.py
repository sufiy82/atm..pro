#without function;
l=list(map(int,input("values").split()))
s=int(input("Enter ele"))
for i in range(0,len(l),1):
    if (l[i]==s):
        print("the",s,"is in the", i ,"index") 
        break
    else:
        print("the s is not found")




#with function;
def linear():   
    l=list(map(int,input("values").split()))
    s=int(input("Enter ele"))
    found=False
    for i in range(0,len(l),1):
          if (l[i]==s):
              print("the",s,"is in the", i ,"index")
              found=True
              break
    else:
        print("the s is not found")
linear()
