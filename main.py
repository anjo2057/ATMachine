
def help():
   # TODO: Displays a list of available commands and their descriptions
   print('help')

def create_user(user_id, name):
    # TODO : 
    # creates a new user with a unique ID and name.
    # - user_id: 5–10 alphanumeric characters.
    # - name: Non-empty string.
    # Errors:
    # - ERROR: User ID already exists.
    # - ERROR: Invalid user ID or name.
    print()

def read_user(user_id): 
    # TODO :     
    # Displays user information.
    # - user_id: Must exist.
    # Errors:
    # - ERROR: User not found.
    print()

def update_user(user_id, new_name):
    # TODO: 
    # Updates the name of an existing user.
    # - user_id: Must exist.
    # - new_name: Non-empty string.
    # Errors:
    # - ERROR: User not found.
    # - ERROR: Invalid new name.
    print() 

def delete_user(user_id): 
    # TODO: 
    # Deletes a user and associated accounts.
    # - user_id: Must exist.
    # Errors:
    # - ERROR: User not found.
    print() 

def deposit(account_id, amount): 
    # TODO: 
    # Adds the specified amount to the account balance.
    # - account_id: 5–10 alphanumeric characters.
    # - amount: Decimal number between 0.01 and 1,000,000.
    # Errors:
    # - ERROR: Invalid amount.
    # - ERROR: Account not found
    print() 


def withdraw(account_id, amount): 
    # TODO: 
    #  Subtracts the specified amount from the account balance.
    # - account_id: Must exist.
    # - amount: Decimal number between 0.01 and current account balance.
    # Errors:
    # - ERROR: Invalid amount.
    # - ERROR: Insufficient funds.
    # - ERROR: Account not found.
    print()


def transfer(source_id, dest_id, amount): 
    # TODO:
    # Transfers money from one account to another.
    # - source_id: Must exist and have sufficient funds.
    # - dest_id: Must be a valid account.
    # - amount: Decimal number between 0.01 and source account balance.
    # Errors:
    # - ERROR: Invalid amount.
    # - ERROR: Insufficient funds.
    # - ERROR: Destination account not found.
    # - ERROR: Source and destination cannot be the same.
    print()

def balance(account_id):
    # TODO:
    # Displays the current balance of the specified account.
    # - account_id: Must exist.
    # Errors:
    # - ERROR: Account not found.
    print()

def history(account_id):
    # TODO:
    # Displays the transaction history of the specified account.
    # - account_id: Must exist.
    # Errors:
    # - ERROR: Account not found.
    print()