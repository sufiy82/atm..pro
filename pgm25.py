d={}
for i in range(0,2,1):
    key=input("subject=")
    value=int(input("marks="))
    d[key]=value
print(d)
print(sum(d.values()))

