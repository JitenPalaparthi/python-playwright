
## Multiple Inheritance

class BankAccount:
    def __init__(self,accno,accname):
        self.account_no=accno
        self.account_name=accname

class BankBranch(BankAccount):
        def __init__(self,branchname):
             self.branch_name=branchname


class BankOne(BankBranch):
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

# in another way to call consgructor


## Multilevel Inheritance,using constructors

print("\nmultilevel inheritance with multilevel constructors")
class BankAccount:
    def __init__(self,accno,accname):
        self.account_no=accno
        self.account_name=accname

class BankBranch(BankAccount):
        def __init__(self,accno,accname,branchname):
             super().__init__(accno,accname)
             self.branch_name=branchname


class BankOne(BankBranch):
     def __init__(self,accno,accname,branchname,ifsc):
         super().__init__(accno,accname,branchname)
         self.ifsc=ifsc
    
     def show(self):
          print("BankOne account Details")
          print("Account No:",self.account_no) 
          print("Account Name:",self.account_name)
          print("Branch Name:",self.branch_name)
          print("Branch IFSC:",self.ifsc)
     

b1 = BankOne(12345,"Jiten P","Guntur-1","00bone00102")

b1.show()


## Multilevel inheritance using MRO **kwargs

print("\nMultilevel inheritance using MRO(Method Resolution Order) **kwargs")

class BankAccount:
    def __init__(self,accno,accname,**kwargs):
        super().__init__(**kwargs)
        self.account_no=accno
        self.account_name=accname

class BankBranch(BankAccount):
        def __init__(self,branchname,**kwargs):
             super().__init__(**kwargs)
             self.branch_name=branchname


class BankOne(BankBranch):
     def __init__(self,accno,accname,branchname,ifsc):
         super().__init__(accno=accno,accname=accname,branchname=branchname)
         self.ifsc=ifsc
    
     def show(self):
          print("BankOne account Details")
          print("Account No:",self.account_no) 
          print("Account Name:",self.account_name)
          print("Branch Name:",self.branch_name)
          print("Branch IFSC:",self.ifsc)
     

b1 = BankOne(12345,"Jiten P","Guntur-1","00bone00102")

b1.show()