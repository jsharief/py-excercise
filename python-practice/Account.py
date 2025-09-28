import uuid
from http.cookiejar import lwp_cookie_str


class Account:
    def __init__(self, name, balance,id):
        self.name = name
        self.balance = balance
        self.id = id

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def __repr__(self):
        return f"Amounter Account(name={self.name}, balance={self.balance})"
   # def __str__(self):
   #     return f"Account(name={self.name}, balance={self.balance})"



ledgers = []
option = "s"
while option != "x" or option != "X":
   print("Option x to exit \n")
   print("Option s to create \n")
   option = input("Enter your choice: ")
   if option == "x":
    print("Thank you for using our application")
    break
   if option == "s":
    print("create your account")
    name = input("Enter your name: ")
    balance = float(input("Enter your balance: "))
    accountNumer = uuid.uuid4()
    account1 = Account(name,balance,accountNumer)
    ledgers.append(account1)
    print("account created {0} with number {1} and balance is {2}".format(account1.name, account1.id, account1.balance))
   if option == "p":
    for ledger in ledgers:
        print("balance: ", ledger.balance)
        print("number: ", ledger.id)
   if option == "d":
       numero = input("Enter your account numer: ")

       accountObj =  [x for x in ledgers if x.id == uuid.UUID(numero)]
       print(accountObj)
       if accountObj is not None:
           amountToDeposit = input("Enter your amount to deposit: ")
           amount = float(amountToDeposit)
           accountObj[0].deposit(amount)
           print("Deposited amount: ", amount)







