t=input("enter string")
print(t)
for i in t:
    if(i.islower()):
        print(i.upper(),end='')
    else:
        print(i.lower(),end='')
