class User:
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.savings = BankAccount(int_rate = 0.02, balance = 0)
		self.checking = BankAccount(int_rate = 0.00, balance = 0)

	def make_deposit(self,amount , **acctName):
		print(acctName)
		self.acctName.deposit(amount)

		# if acctName == 'savings':
		# 	self.savings.deposit(amount)
		# 	return self
		# elif acctName == 'checking':
		# 	self.checking.deposit(amount)
		# 	return self
		# else:
		# 	print('Invalid account name.')
		# 	return self

	def make_withdrawl(self, acctName, amount):
		if acctName == 'savings':
			self.savings.withdraw(amount)
			return self
		elif acctName == 'checking':
			self.checking.withdraw(amount)
			return self
		else:
			print('Invalid account name.')
			return self


	def display_user_balance(self, acctName):
		if acctName == 'savings':
			print(f"{self.name}'s savings account Balance is: ${self.savings.balance}")
			return self
		elif acctName == 'checking':
			print(f"{self.name}'s checking account Balance is: ${self.checking.balance}")
			return self
		else:
			print('Invalid account name.')
			return self
	
	def transfer_money(self, acctName, amount, user, toAcctName):
		if (acctName == 'savings' or acctName == 'checking') and (toAcctName == "savings" or toAcctName == "checking"):
			if acctName == 'savings':
				if self.savings.balance >= amount:
					self.savings.withdraw(amount)
					if toAcctName == 'savings':
						user.savings.deposit(amount)
						print(f"{self.name} transfered ${amount} to {user.name}'s account")
						return self
					elif toAcctName == 'checking':
						user.checking.deposit(amount)
						print(f"{self.name} transfered ${amount} to {user.name}'s account")
						return self
				else:
					print("Insufficient Funds")
					return self
			if acctName == 'checking':
				if self.checking.balance >= amount:
					self.checking.withdraw(amount)
					if toAcctName == 'savings':
						user.savings.deposit(amount)
						print(f"{self.name} transfered ${amount} to {user.name}'s account")
						return self
					elif toAcctName == 'checking':
						user.checking.deposit(amount)
						print(f"{self.name} transfered ${amount} to {user.name}'s account")
						return self
				else:
					print("Insufficient Funds")
					return self
		else:
			print('Invaild Account Name')


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

John.make_deposit(acctName = 'savings',amount = 100)

# John.transfer_money('savings',50,Sally,'checking')
# Sally.display_user_balance('checking')
