class Bank:
    def __init__(self,name,acc_no):
        self.name=name
        self.Account_no=acc_no
        self.balance=0
    def display(self):
       print()
       print("-------Account Details-------")
       print("Account Holder name:",self.name)
       print("Account number:",self.Account_no)
    def desposit(self,deposit):
       self.dp=deposit
       self.balance=self.balance+self.dp
       print("amount add")
    def withdraw(self,w):
       if w<self.balance:
          self.balance=self.balance-w
          print("amount withdraw")
       else:
          print("Less amount")

    def display_balance(self):
        print(self.balance)
name=str(input("enter the name:"))
acc_no=int(input("Account number:"))
obj=Bank(name,acc_no)
obj.display()
print()
print()
print("1.Deposit")
print("2.withdraw")
print("3.view")
print("4.exit")
while (True):
    n=int(input("enter the choice"))
    if n==1:
      deposit=int(input("enter the amount"))
      obj.desposit(deposit) # Call the correct 'deposit' method
    elif n==2:
      wrd=int(input("enter the amount"))
      obj.withdraw(wrd) # Call the correct 'withdraw' method
    elif n==3:
      print("view")
      obj.display_balance()
    elif n==4:
      print("exit")
      break
else:
      print("invaild inputs")
