from Bank import Account

if __name__ == '__main__':
    # Get the user's name
    name = input('''
    Welcome to The Bank! Let's get you setup with a Checking and a Savings.

    Please enter your name: 
    ''')
    
    # Create their accounts
    checking = Account(name, 'Checking')
    savings = Account(name, 'Savings')

    print(f'''
    Thank you, {name}!
    Your accounts have been created.

    Checking Account Number: {checking.number}
    Savings Account Number: {savings.number}''')
    
    # App UI
    while True: 
        # Selecting the account to perform transactions with
        account_selection = input('''
    Which account are we working with?

    1) Checking
    2) Savings
    3) Exit

    Please select an account: ''')

        match account_selection:
            case '1':
                account = checking
            case '2':
                account = savings
            case '3':
                quit()
            case _:
                print('\n    Please enter a valid selection.')
                continue

        # Selecting the type of transaction
        task_selection = input(f'''
    How can we help you with your {account.type} today?

        1) View balance
        2) Make a deposit
        3) Make a withdrawl
        4) Make a transfer
        5) Exit

    Please enter a number: ''')

        match task_selection:
            case '1':
                print(account.show_balance())
            case '2':
                amount = float(input(f'''
    How much would you like to deposit into your {account.type} account?
    '''))
                print(account.deposit(amount))
            case '3':
                amount = float(input(f'''
    How much would you like to withdraw from your {account.type} account?
    '''))
                print(account.withdraw(amount))
            case '4':
                amount = float(input(f'''
    How much would you like to transfer from your {account.type} account?
    It will go into your other existing accout.
    '''))
                if account.type == 'Checking':
                    print(account.transfer(savings, amount))
                else:
                    print(account.transfer(checking, amount))
            case '5':
                quit()
            case _:
                print('\n    Please select a valid selection')
                continue



            
