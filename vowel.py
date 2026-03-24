a="noorain@123"
s=['a','e','i','o','u']
c=0
oval=0
const=0
char=0
digit=0
splch=0
for z in a:
    if(z in s):
        c+=1
        print("vowels",z)
        oval+=1
    else:
        print("consonents",z)
        const+=1
            
    if(z.isalpha()):
        print("alphabet",z)
        char+=1
    elif(z.isdigit()):
        print("digit",z)
        digit+=1
    else:
        print("spl char",z)
        splch+=1
print("oval",oval,"consonent",const,"alpha",char,"inte",digit,"zaiba",splch)
