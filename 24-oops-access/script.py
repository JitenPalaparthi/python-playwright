
class BankAccount:

    def __init__(self,account_holder,balance):
        self.account_holder= account_holder # public 
        self._balance = balance # protected single underscore _ is protected
        self.__pin = "1234" # private double underscore __ is private

# public, private protected

    def deposit(self,amount):
        self._balance+= amount
        print(f"Deposited: {amount}")

    def withdraw(self,amount):
        if amount<= self._balance:
             self._balance-= amount
             print(f"Withdraw: {amount}")
        else:
            print("insufficient balance")

    def get_balance(self):
        return self._balance
    
    def __show_pin(self):
        print("PIN:",self.__pin)
    
    def access_private_pin(self):
        self.__show_pin()



class SavingsAccount(BankAccount):
    def __init__(self,account_holder,balance,interest_rate):
        super().__init__(account_holder=account_holder,balance=balance)
        self.interest_rate=interest_rate

    def add_interest(self):
        interest= self._balance *self.interest_rate/100
        self._balance+=interest
        print(f"interest: added:{interest}")

# method overriding
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        #return super().withdraw(amount)
        if amount<= self._balance+5000:
            self._balance==amount 
            print("Overdraft supported")
        else:
            print("Limit exceeded")


s= SavingsAccount("Jiten",10000,5)
s.deposit(2000)
s.withdraw(3000)
s.add_interest()
print(s.get_balance())

accounts = [SavingsAccount("Jiten",10000,5),CurrentAccount("Jyothi",20000)]

for a in accounts:
    # print(SavingsAccount.mro())
    a.withdraw(5000)
    try:
        a.add_interest()
    except AttributeError:
        print("Method not supported")
    finally:
        print("account holder:",a.account_holder,"Balance:",a.get_balance())
