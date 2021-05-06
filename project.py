# for this assignment, our User class will no longer have a self.account_balance 
# attribute. Instead, we will replace this attribute's value in our __init__ method 
# with an instance of a BankAccount, and use the name of self.account. That means our
# make_deposit (and other methods referencing self.account_balance) need to be updated!
# That's the goal of this assignment.

# Remember in our User methods, we are going to now be accessing the BankAccount class through our self.account attribute, like so:
# class User:
#     def example_method(self):
#         self.account.deposit(100)		# we can call the BankAccount instance's methods
#     	print(self.account.balance)		# or access its attributes

# Make sure that by the end of this assignment that you:
#     have both the User and BankAccount classes in the same file for your assignment
#     only create BankAccount instances inside of the User's __init__ method
#     only call BankAccount methods inside of the methods in the User class


# 1. Update the User class __init__ method

# 2. Update the User class make_deposit method

# 3. Update the User class make_withdrawal method

# 4. Update the User class display_user_balance method

# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to


class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(balance = 0, interest = 0.01)

    def display_user_balance(self):
        print(f"User Name: {self.name}\nAccount Balance: ${self.account.balance}")
        return self

class BankAccount:
    def __init__(self, balance, interest):
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

    def yield_interest(self):           #increases the account balance by the current balance * the interest rate (as long as the balance is positive)
        if self.balance > 0:
            self.balance += self.interest *self.balance 
        return self


jim = User("Jim")
jim.account.make_deposit(133).make_deposit(133).make_deposit(134).make_withdrawal(13)
jim.display_user_balance()

jake = User("Jake")
jake.account.make_deposit(50).make_deposit(51).make_withdrawal(1).make_withdrawal(1)
jake.display_user_balance()

john = User("John")
john.account.make_deposit(72).make_withdrawal(3).make_withdrawal(6).make_withdrawal(9)
john.display_user_balance()

jim.account.transfer_money(john, 18)
jim.display_user_balance()
jake.display_user_balance()