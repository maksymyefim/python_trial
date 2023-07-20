class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit):
        self.balance = self.balance + deposit
        print("We added {} to your balance".format(deposit))

    def withdraw(self, withdraw):
        self.withdraw = self.balance - withdraw
        while self.withdraw > self.balance:
            print("Withdraw Accepted")
        else:
            print("Funds are unavailable")


acct1 = Account('Jose', 100)

print(acct1.owner)
print(acct1.balance)
acct1.withdraw(75)
print(acct1.balance)
