d={}
for i in range(0,2,1):
    key=input("name=")
    value=int(input("age="))
    d[key]=value
print(d)
sum=0
for value in d.values():
    sum=sum+value
print(sum)


   
