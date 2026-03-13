from abc import ABC, abstractmethod
class ATMBase(ABC):
    @abstractmethod
    def check_balance(self):
        pass
    @abstractmethod
    def deposite(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class ATM(ATMBase):
    def __init__(self):
        self.__balance=10000
        self.transactions=[]
    def check_balance(self):
        print("your balance:",self.__balance)
    def deposite(self):
        amount=int(input("Enter amount to deposite:"))
        self.__balance=self.__balance+amount
        self.transactions.append("Deposited"+str(amount))
        print("Deposite successfull")
    def withdraw(self):
        amount=int(input("Enter amount to withdraw:"))
        if amount<=self.__balance:
            self.__balance=self.__balance-amount
            self.transactions.append("withdraw"+str(amount))
            print("please collect your money")
        else:
            print("insufficeint balance")
    def show_transactions(self):
        print("taransaction history")
        for t in self.transactions:
            print(t)
atm=ATM()
while True:
    print("\===== ATM MENU =====")
    print("1.check balance")
    print("2.Deposite")
    print("3.withdraw")
    print("4.transaction")
    print("5.exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        atm.check_balance()
    elif choice==2:
            atm.deposite()
    elif choice==3:
            atm.withdraw()
    elif choice==4:
            atm.show_transactions()
    elif choice==5:
            print("thank you")
            break
    else:
        print("invalid option")
            
    
        

    
    
    
   
