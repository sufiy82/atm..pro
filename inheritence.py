class parent:
    def show(self):
        print("this is parent class")
class child(parent):
    def pri(self):
        print("this is my child class")
p=parent()
p.show()
c=child()
c.pri()
c.show()


class car:
    def show(self):
        print("this is my verna car")
class scooty(car):
    def pri(self):
        print("this is my dio scooty")
c=car()
c.show()
s=scooty()
s.pri()
s.show() 
