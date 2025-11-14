import argparse
import sys


def main():
    input_data = open(sys.argv[1]).read()  # Read all input from standard
    # print(input_data)

    # May not needed if we look in the spec
    if len(sys.argv) < 2 or len(input_data) < 2:
        print("Usage: python3 main.py <file.txt>", file=sys.stderr)
        sys.exit(1)

    # Process the input data
    process_input()


def process_input():
    filename = sys.argv[1]
    with open(filename, "r+") as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            # print(line)
            line_to_process = line
            if line_to_process.startswith("help"):
                help()
            if line_to_process.startswith("create_user"):
                x = line_to_process.split()
                create_user(x[1], x[2])
            if line_to_process.startswith("read_user"):
                x = line_to_process.split()
                read_user(x[1])
            if line_to_process.startswith("update_user"):
                x = line_to_process.split()
                update_user(x[1], x[2])
            if line_to_process.startswith("delete_user"):
                x = line_to_process.split()
                delete_user(x[1])
            if line_to_process.startswith("deposit"):
                x = line_to_process.split()
                deposit(x[1], x[2])
            if line_to_process.startswith("withdraw"):
                x = line_to_process.split()
                withdraw(x[1], x[2])
            if line_to_process.startswith("transfer"):
                x = line_to_process.split()
                transfer(x[1], x[2], x[3])
            if line_to_process.startswith("balance"):
                x = line_to_process.split()
                balance(x[1])
            if line_to_process.startswith("history"):
                x = line_to_process.split()
                history(x[1])
            if line_to_process.startswith("add_account"):
                x = line_to_process.split()
                add_account(x[1], x[2])
            if line_to_process.startswith("remove_account"):
                x = line_to_process.split()
                remove_account(x[1])

            if i > len(lines) - 2:
                # ne = lines[i + 1] # you may want to check that i < len(lines)
                # print(' end of file ')
                break


## Global dictionary to store user data and accounts

Users = {}

BankAccounts = {}


# Displays a list of available commands and their descriptions
def help():
    print("help:")
    print("  create_user <user_id> <name>  Create a new user")
    print("  read_user <user_id>            Read user information")
    print("  update_user <user_id> <name>   Update user information")
    print("  delete_user <user_id>          Delete a user")
    print("  deposit <account_id> <amount>  Deposit money")
    print("  withdraw <account_id> <amount> Withdraw money")
    print("  transfer <source_id> <dest_id> <amount>  Transfer money")
    print("  balance <account_id>           Check account balance")
    print("  history <account_id>           View transaction history")


# creates a new user with a unique ID and name.
# - user_id: 5–10 alphanumeric characters.
# - name: Non-empty string.
# Errors:
# - ERROR: User ID already exists.
# - ERROR: Invalid user ID or name.
def create_user(user_id, name):
    if user_id in Users:
        print("ERROR: User ID already exists.")
    elif not (5 <= len(user_id) <= 10) or not name:
        print("ERROR: Invalid user ID or name.")
        if len(user_id) < 5 or len(user_id) > 10:
            print("User ID length issue:", len(user_id))
            print("Should be between 5 and 10 characters.")
    else:
        Users[user_id] = name
        print("User created:", user_id, name)

    # Displays user information.
    # - user_id: Must exist.
    # Errors:
    # - ERROR: User not found.


def read_user(user_id):
    # TODO :
    if user_id in Users:
        print("User found:", user_id, Users[user_id])
    else:
        print("ERROR: User not found.")

# - user_id: Must exist.
# - new_name: Non-empty string.
# Errors:
# - ERROR: User not found.
# - ERROR: Invalid new name.

def update_user(user_id, new_name):
    if user_id in Users:
        if new_name:
            Users[user_id] = new_name
            print("User updated:", user_id, new_name)
        else:
            print("ERROR: Invalid new name.")
    else:
        print("ERROR: User not found.")



# Deletes a user and associated accounts.
# - user_id: Must exist.
# Errors:
# - ERROR: User not found.

def delete_user(user_id):
    if user_id in Users:
        del Users[user_id]
        print("User deleted:", user_id)
    else:
        print("ERROR: User not found.")


# Adds the specified amount to the account balance.
# - account_id: 5–10 alphanumeric characters.
# - amount: Decimal number between 0.01 and 1,000,000.
# Errors:
# - ERROR: Invalid amount.
# - ERROR: Account not found
def deposit(account_id, amount):
    if account_id in BankAccounts:
        try:
            amt = float(amount)
            if 0.01 <= amt <= 1000000:
                BankAccounts[account_id]["balance"] += amt
                BankAccounts[account_id]["history"].append(f"Deposited: {amt}")
                print(
                    f"Deposited {amt} to account {account_id}. New balance: {BankAccounts[account_id]['balance']}"
                )
            else:
                print("ERROR: Invalid amount.")
        except ValueError:
            print("ERROR: Invalid amount.")
    else:
        print("ERROR: Account not found")


#  Subtracts the specified amount from the account balance.
# - account_id: Must exist.
# - amount: Decimal number between 0.01 and current account balance.
# Errors:
# - ERROR: Invalid amount.
# - ERROR: Insufficient funds.
# - ERROR: Account not found.
def withdraw(account_id, amount):
    if account_id in BankAccounts:
        try:
            amt = float(amount)
            if 0.01 <= amt <= balance(account_id):
                BankAccounts[account_id]["balance"] -= amt
                BankAccounts[account_id]["history"].append(f"Withdraw: {amt}")
                print(
                    f"Withdrew {amt} from account {account_id}. New balance: {BankAccounts[account_id]['balance']}"
                )
            else:
                if amt > balance(account_id):
                    print("ERROR: insufficient funds.")
                if amt < 0.01:
                    print("ERROR: Invalid amount")
        except ValueError:
            print("ERROR: Invalid amount")
    else:
        print("ERROR: Account not found.")


# Transfers money from one account to another.
# - source_id: Must exist and have sufficient funds.
# - dest_id: Must be a valid account.
# - amount: Decimal number between 0.01 and source account balance.
# Errors:
# - ERROR: Invalid amount.
# - ERROR: Insufficient funds.
# - ERROR: Destination account not found.
# - ERROR: Source and destination cannot be the same.
def transfer(source_id, dest_id, amount):
    if source_id == dest_id:
        print("ERROR: Source and destination cannot be the same.")
        return

    withdraw(source_id, amount)
    deposit(dest_id, amount)


# Displays the current balance of the specified account.
# - account_id: Must exist.
# Errors:
# - ERROR: Account not found.
def balance(account_id):
    if account_id in BankAccounts:
        bal = BankAccounts[account_id]["balance"]
        print(f"Account {account_id} balance: {bal}")
        return bal
    else:
        print("ERROR: Account not found.")
        return 0.0

# Displays the transaction history of the specified account.
# - account_id: Must exist.
# Errors:
# - ERROR: Account not found.

def history(account_id):
    if account_id in BankAccounts:
        history = BankAccounts[account_id]["history"]
        print(f"Account {account_id} history: {history}")
        return history
    else:
        print("ERROR: Account not found")


## NOT DESRCRIBED IN SPEC BUT NEEDED FOR TESTS
# Adds a new bank account for an existing user.
# - user_id: Must exist.
# - account_id: 5–10 alphanumeric characters.
# Errors:
# - ERROR: User not found.
# - ERROR: Account ID already exists.
def add_account(user_id, account_id):
    if user_id in Users:
        if account_id not in BankAccounts:
            BankAccounts[account_id] = {
                "user_id": user_id,
                "balance": 0.0,
                "history": [],
            }
            print("Account added:", account_id)
        else:
            print("ERROR: Account ID already exists.")
    else:
        print("ERROR: User not found.")


# Removes an existing bank account.
# - account_id: Must exist.
# Errors:
# - ERROR: Account not found.
def remove_account(account_id):
    if account_id in BankAccounts:
        del BankAccounts[account_id]
        print("Account removed:", account_id)
    else:
        print("ERROR: Account not found.")


if __name__ == "__main__":
    main()
