n=[2,4,6,8]
for z in n:
    c=0
    if(z==1):
        print("not prime")
    else:
        for i in range(1,z+1,1):
            if z%i==0:
                c+=1
            if c==1:
                print("prime",z)
    
   
    
   
    
    
    
