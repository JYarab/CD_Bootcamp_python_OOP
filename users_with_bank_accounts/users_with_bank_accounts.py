class User:
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.account = BankAccount(int_rate = 0.02, balance = 0)

	def make_deposit(self, amount):
		self.account.deposit(amount)
		print(f"{self.name} desposited ${amount} into their account")
		return self

	def make_withdrawl(self, amount):
		self.account.withdraw(amount)
		return self


	def display_user_balance(self):
		print(f"{self.name}'s account Balance is: ${self.account.balance}")
		return self
	
	def transfer_money(self, amount, user):
		if self.account.balance >= amount:
			self.account.withdraw(amount)
			user.account.deposit(amount)
			print(f"{self.name} transfered ${amount} to {user.name}'s account")
			return self
		else:
			print("Insufficient Funds")
			return self


class BankAccount:
	def __init__(self, int_rate, balance):
		self.int_rate = int_rate
		self.balance = balance
		
	def deposit(self, amount):
		self.balance += amount
		return self

	def withdraw(self, amount):
		if self.balance >= amount:
			self.balance -= amount
			return self
		else:
			print("Insufficient Funds")
			return self

	def display_account_info(self):
		print(f"Current balance is ${'%.2f'%self.balance}. Current interest rate is {self.int_rate*100}%")
		return self

	def yield_interest(self):
		self.balance += round(self.balance*self.int_rate,2)
		return self



John = User('John', 'J_Jones@gmail.com')
Bob = User('Bob', 'Bob_Villa@gmail.com')
Sally = User('Sally', 'Sally.Moris@yahoo.com')

John.make_deposit(50)
John.make_deposit(50)
John.make_deposit(50)
John.make_withdrawl(25)

John.display_user_balance()

Bob.make_deposit(50)
Bob.make_deposit(100)
Bob.make_withdrawl(10)
Bob.make_withdrawl(20)

Bob.display_user_balance()

Sally.make_deposit(100)
Sally.make_withdrawl(10)
Sally.make_withdrawl(10)
Sally.make_withdrawl(10)

Sally.display_user_balance()

John.transfer_money(10, Sally)

John.display_user_balance()
Sally.display_user_balance()