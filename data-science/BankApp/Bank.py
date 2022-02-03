from random import randint

# Class definitions for a simple banking app.

class Account:
    
    def __init__(self, customer_name: str, account_type: str) -> None:
        '''Given an owner name, create an account instance for the customer'''
        self.owner = customer_name
        self.number = randint(100000, 999999)
        self.balance = 0
        self.type = account_type

    def show_balance(self) -> str:
        '''Show the balance of the account'''
        return f'\n    The balance of your {self.type} account is ${"{:.2f}".format(self.balance)}'
    
    def deposit(self, amount: float) -> str:
        '''Deposit a specified amount into the account'''
        self.balance += round(amount, 2)
        return f'''
    You have deposited ${"{:.2f}".format(amount)} into your account.
    Your account balance is now ${"{:.2f}".format(self.balance)}'''

    def withdraw(self, amount: float) -> str:
        '''Withdraw a specified amount from the account'''
        if amount > self.balance:
            return '\n    Insufficient Funds'
        else:
            self.balance -= round(amount, 2)
            return f'''
    You have withdrawn ${"{:.2f}".format(amount)} from your account.
    Your account balance is now ${"{:.2f}".format(self.balance)}'''

    def transfer(self, other, amount: float) -> str:
        '''Transfer a specified amount from one account to another'''
        if amount > self.balance:
            return '\n    Insufficient Funds'
        else:
            self.balance -= round(amount, 2)
            other.balance += round(amount, 2)
            return f'''
    You have transferred ${"{:.2f}".format(amount)} from your {self.type} account to your {other.type} account.
    Your account balances are:
    {self.type}: ${"{:.2f}".format(self.balance)}
    {other.type}: ${"{:.2f}".format(other.balance)}'''

        
