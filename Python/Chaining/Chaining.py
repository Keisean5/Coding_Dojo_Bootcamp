class User:
    def __init__(self, name_parameter, email_parameter):
        self.name = name_parameter
        self.email = email_parameter
        self.account_balance = 1000

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        print(f'{self.name} withdrew {amount}')
        return self

    def make_deposit(self, amount):
        self.account_balance += amount
        print(f'{self.name} deposited {amount}')
        return self


guido = User('Guido', 'gg@gmail.com') 
guido.make_deposit(200).make_deposit(100).make_deposit(300).make_withdrawal(50)
# print(guido.name)
# print(guido.email)
print(f'{guido.name} now has {guido.account_balance}')
print('------------------------')
monty = User('Monty', 'mm@gmail.com')
monty.make_deposit(200).make_deposit(400).make_withdrawal(150).make_withdrawal(50)
# print(monty.name)
# print(monty.email)
print(f'{monty.name} now has {monty.account_balance}')
print('------------------------')
sean = User('Sean', 'ss@gmail.com')
sean.make_withdrawal(150).make_withdrawal(250).make_withdrawal(450).make_deposit(550)
# print(sean.name)
# print(sean.email)
print(f'{sean.name} now has {sean.account_balance}')