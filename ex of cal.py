from abc import ABC,abstractmethod
class calci(ABC):
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass
    @abstractmethod
    def mul(self):
        pass
    @abstractmethod
    def div(self):
        pass
    @abstractmethod
    def mod(self):
        pass
    @abstractmethod
    def expo(self):
        pass
class cal(calci):

    def __init__(self):
        self.a=9
        self.b=19
    def add(self):
        print("Addition",self.a+self.b)
    def sub(self):
        print("substraction",self.a-self.b)
    def mul(self):
        print("multiplication",self.a*self.b)
    def div(self):
        print("division",self.a/self.b)
    def mod(self):
        print("modulud",self.a%self.b)
    def expo(self):
        print("exponental",self.a**self.b)
s=cal()
while True:
    print("\===== CAL MENU =====")
    print("1.add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("5.mod")
    print("6.expo")
    choice=int(input("Enter your choice:"))
    if choice==1:
        s.add()
    elif choice==2:
        s.sub()
    elif choice==3:
        s.mul()
    elif choice==4:
        s.div()
    elif choice==5:
        s.mod()
    elif choice==6:
        s.expo()
    elif choice==7:
        print("thank you")
        break
    else:
        print("invalid option")
          
          

        
