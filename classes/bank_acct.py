class BankAccount:
    def __init__(self, balance):
        self.balance = balance


    def deposit(self, amount):
        self.balance = amount + self.balance
        return f"deposited {amount} successfully"
    
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            return f"Withdrew {amount}, new balance: {self.balance}" 
        else:
            return "Insufficient funds"
        
sum = BankAccount(100000)
print(sum.withdraw(100))
print(sum.withdraw(100))


        