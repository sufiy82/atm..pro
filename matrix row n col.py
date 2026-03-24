Array=[1,2,3,4]
r=int(input("Enter row size"))
c=int(input("Enter column size"))
l=[]
for i in range(0,r,1):
    m=[]
    for i in range(0,c,1):
        ele=int(input("ele="))
        m.append(ele)
    l.append(m)
for i in range(0,r,1):
    print(l[i])
