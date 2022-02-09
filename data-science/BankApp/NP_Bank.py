import numpy as np

class NP_Bank:
    '''A bank class using a numpy array of 2 accounts (Checking and Savings)'''
    def __init__(self) -> None:
        self.balances = np.zeros(2)

    def show_balances(self) -> str:
        '''Print the balances of the accounts'''
        return f'Your balances are:\nChecking: ${self.balances[0]}\nSavings: ${self.balances[1]}'

    def show_stats(self) -> str:
        '''Print the mean, median, and stdev of the accounts'''
        self.stats = np.array([np.mean(self.balances), np.median(self.balances), np.std(self.balances)])
        return f'Your account stats are:\nMean: {self.stats[0]}\nMedian: {self.stats[1]}\nStandard Deviation: {self.stats[2]}'

    def show_inverse(self) -> str:
        '''Print the inverse of the account balances'''
        self.inv_bal = np.multiply(self.balances, -1)
        return f'The inverse balances of your accounts are:\nChecking: ${self.inv_bal[0]}\nSavings: ${self.inv_bal[1]}'

    def deposit(self, amount: float, account: int) -> str:
        '''Deposit a given amount into a specified account; 0 for checking, and 1 for savings'''
        account_name = 'Checking' if account == 0 else 'Savings'
        self.balances[account] += amount
        return f'You deposited ${amount} to your {account_name} account.\nYour balance is now ${self.balances[account]}'

    def withdraw(self, amount: float, account: int) -> str:
        '''Withdraw a given amount from a specified account; 0 for checking, and 1 for savings'''
        account_name = 'Checking' if account == 0 else 'Savings'
        self.balances[account] -= amount
        return f'You withdrew ${amount} from your {account_name} account.\nYour balance is now ${self.balances[account]}'

    def gift(self, amount: float) -> str:
        '''Gift a certain amount to all accounts'''
        self.balances = np.add(self.balances, amount)
        return f'You gifted ${amount} into all accounts. Your balances are:\nChecking: ${self.balances[0]}\nSavings: ${self.balances[1]}'


