
## Multiple Inheritance

class BankAccount:
    def __init__(self,accno,accname):
        self.account_no=accno
        self.account_name=accname

class BankBranch:
        def __init__(self,branchname):
             self.branch_name=branchname


class BankOne(BankAccount,BankBranch):
     def __init__(self,accno,accname,branchname,ifsc):
          BankAccount.__init__(self,accno,accname)
          BankBranch.__init__(self,branchname)
          self.ifsc=ifsc
    
     def show(self):
          print("BankOne account Details")
          print("Account No:",self.account_no) 
          print("Account Name:",self.account_name)
          print("Branch Name:",self.branch_name)
          print("Branch IFSC:",self.ifsc)
     

b1 = BankOne(12345,"Jiten P","Guntur-1","00bone00102")

b1.show()

