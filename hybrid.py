class cal:
    def add(self):
      a=5
      b=2
      print(a+b)
class cal1(cal):
    def sub(self):
      a=2
      b=1
      print(a-b)
class cal2(cal):
    def prod(self):
       a=5
       b=3
       print(a*b)
c=cal()
c.add()
c=cal1()
c.sub()
c=cal2()
c.prod()
