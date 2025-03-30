class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 500
        self.max_withdraw = 100000

    def get_balance(self):
        return f"your current balance is {self.balance}"
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"new balance after {amount} deposit {self.balance}"
        else:
            return "Invalid amount"
    
    def withdraw(self, amount):
        if amount >= self.min_withdraw and amount <= self.max_withdraw and self.balance >= amount  :
            self.balance -= amount
            return f"new balance after {amount} withdraw {self.balance}"
        else:
            return "withdraw condition not met"


dbbl = Bank(50000)
print(dbbl.withdraw(500))
print(dbbl.deposit(5000))
print(dbbl.get_balance())