a="hELLo worLD"
s=""
for i in a:
    if "a" <= i  <= "s":
        s=chr(ord(i)-32)
    elif "A" <=i <= "S":
        s=chr(ord(i)+32)
else:
    s+=1
    print(s)
