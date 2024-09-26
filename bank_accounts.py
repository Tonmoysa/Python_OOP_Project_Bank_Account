class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,initialAmount,acctName):
        self.balance=initialAmount
        self.name=acctName
        print(f'Account holder name:{self.name} created .\nBalance={self.balance:.2f}')
    
    def getBalance(self):
        print(f"Account holder name:{self.name} created .\nBalance={self.balance:.2f}")

    def depositBalance(self,amount):
        self.balance=self.balance+amount
        print('\nDeposit Completed Sucessfully!')
        self.getBalance()
    
    def viableTransaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(f"Sorry,account {self.name} has balance of{self.balance:.2f}")
        
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance=self.balance-amount
            print(f'\n withdraw comepleted')
            self.getBalance()
        except BalanceException as error:
            print(f'withdraw interrupted.{error}')
        
    def transfer(self,amount,account):
        try:
            print(f"\n**********\n\nBegining Transfer")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.depositBalance(amount)
            print(f'Transfer complete')
        except BalanceException as error:
            print(f'\nTransfer interupted{error}')
    


class Interest(BankAccount):
    def depositBalance(self, amount):
        self.balance=self.balance+(amount*1.5)
        print(f'\nDeposit Complete')
        self.getBalance()
        

class SavingAccount(Interest):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee=5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount+self.fee)
            self.balance=self.balance-(amount+self.fee)
            print(f'\nWithdraw complete')
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interupted.{error}')
            
        

