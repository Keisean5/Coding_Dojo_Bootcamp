

class User:
    def __init__(self, name_parameter, email_parameter):
        self.name = name_parameter
        self.email = email_parameter
        self.account_balance = 1000

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def make_deposit(self, amount):
        self.account_balance += amount


guido = User('Guido', 'gg@gmail.com') 
guido.make_deposit(200)
guido.make_deposit(100)
guido.make_deposit(300)
guido.make_withdrawal(50)
# print(guido.name)
# print(guido.email)
print(guido.account_balance)

monty = User('Monty', 'mm@gmail.com')
monty.make_deposit(200)
monty.make_deposit(400)
monty.make_withdrawal(150)
monty.make_withdrawal(50)
# print(monty.name)
# print(monty.email)
print(monty.account_balance)

sean = User('Sean', 'ss@gmail.com')
sean.make_withdrawal(150)
sean.make_withdrawal(250)
sean.make_withdrawal(450)
sean.make_deposit(550)
# print(sean.name)
# print(sean.email)
print(sean.account_balance)

