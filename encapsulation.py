class phone:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
ph=phone(100)
print(ph.get_balance())
