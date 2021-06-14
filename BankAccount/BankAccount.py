class BankAccount:
	def __init__(self, int_rate = 0.001, balance = 0):
		self.int_rate = int_rate
		self.balance = balance
		
	def deposit(self, amount):
		self.balance += amount
		return self

	def withdraw(self, amount):
		self.balance -= amount
		return self

	def display_account_info(self):
		print(f"Current balance is ${'%.2f'%self.balance}. Current interest rate is {self.int_rate*100}%")
		return self

	def yield_interest(self):
		self.balance += round(self.balance*self.int_rate,2)
		return self

Acct_8675309 = BankAccount()
Acct_5551234 = BankAccount()

Acct_8675309.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()

Acct_5551234.deposit(100).deposit(100).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()