L=["Aradhya","Arun","Ramya","Raju"]
v=['a','e','i','o','u','A','E','I','O','U']
for name in L:
    c=0
    for ch in name:
        if(ch in v):
            c=c+1
    print(name,"=",c)
