class User:
    def __init__(self, name):
        self.name = name
        self.account = []  

    def make_deposit(self, amount, num):             #increases the account balance by the given amount
        self.account[num].make_deposit(amount)
        return self

    def make_withdrawal(self, amount, num):          #decreases the account balance by the given amount or prints a message and deduct $5
        self.account[num].make_withdrawal(amount)
        return self

    def display_user_balance(self, num):
        print(f"User Name: {self.name}\nBalance in Account {num}: ${self.account[num].balance}")
        return self
    
    def transfer_money(self, other_user, amount, num1, num2):
        self.account[num1].make_withdrawal(amount)
        other_user.account[num2].make_deposit(amount)

    def yield_interest(self, num):           #increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        if self.account[num].balance > 0:
            self.account[num].balance += self.account[num].interest * self.account[num].balance 
        return self

    def create_account(self, balance = 0, interest = 0.01):
        self.account.append(BankAccount(balance, interest))
        return len(self.account)-1


class BankAccount:
    def __init__(self, balance = 0, interest= 0.01):
        self.balance = balance
        self.interest = interest

    def make_deposit(self, amount):           #increases the account balance by the given amount
        self.balance += amount
        return self

    def make_withdrawal(self, amount):           #decreases the account balance by the given amount or prints a message and deduct $5
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.account.balance += amount
        return self

    def yield_interest(self):           #increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        if self.balance > 0:
            self.balance += self.interest * self.balance 
        return self


jim = User("Jim")
x = jim.create_account()
# print(f"x = {x}")
# print(f"# of accounts for jim = {len(jim.account)}")
jim.make_deposit(133, x).make_deposit(133, x).make_deposit(134, x).make_withdrawal(13, x).display_user_balance(x)
y = jim.create_account()
# print(f"y = {y}")
# print(f"# of accounts for jim = {len(jim.account)}")
jim.make_deposit(133, y).make_deposit(133, y).make_deposit(134, y).make_withdrawal(13, y).display_user_balance(y)

jake = User("Jake")
jake.create_account()
jake.make_deposit(50, 0).make_deposit(51, 0).make_withdrawal(1, 0).make_withdrawal(1, 0).display_user_balance(0)

john = User("John")
john.create_account()
john.make_deposit(72, 0).make_withdrawal(3, 0).make_withdrawal(6, 0).make_withdrawal(9, 0).display_user_balance(0)

jim.transfer_money(john, 18, 0, 0)
jim.display_user_balance(0)
john.display_user_balance(0)

