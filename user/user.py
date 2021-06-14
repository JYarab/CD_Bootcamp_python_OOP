class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        print(f"{self.name} desposited ${amount} into their account")

    def make_withdrawl(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{self.name} withdrew ${amount} from their account")
        else:
            print("Insufficient Funds")

    def display_user_balance(self):
        print(f"{self.name}'s Account Balance is: ${self.account_balance}")
    
    def transfer_money(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        print(f"{self.name} trasfered ${amount} to {user.name}'s account")

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