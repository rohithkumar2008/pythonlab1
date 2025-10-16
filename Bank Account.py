class Bank:
    def __init__(self,accountnum,balance):
        self.accountnum=accountnum
        self.balance=balance
        print("Account created with the number: ",accountnum)
        print("Initial balance: ",self.balance)

    def dis_balance(self):
        print("Your Account Balance: ",self.balance)

    def deposit(self,amount):
        self.balance+=amount
        print("Amount deposited: ",amount,"Available balances: ",self.balance)

    def withdraw(self,withamount):
        if self.balance<withamount:
            print("Insufficient balance")
        else:
            self.balance-=withamount
            print("Amount withdrawn: ",withamount) 

class Savings(Bank):
    def __init__(self,accountnum,balance,interest):
        super().__init__(accountnum,balance)
        self.interest=interest

    def applyinterest(self):
        interest=self.balance*(self.interest/100)
        self.balance+=interest
        print("Applied interest: ",interest)
        print("Total balance with interest: ",self.balance) 

obj=Savings(123,1000,5) 
obj.deposit(500) 
obj.withdraw(300) 
obj.dis_balance() 
obj.applyinterest()
