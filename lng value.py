s="the longest word is the string programming"
m=s.split()
t=""
for i in m:
    if(len(t)<len(i)):
        t=i      
print(t)
