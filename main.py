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


def deposit(account_id, amount):
    # TODO:
    # Adds the specified amount to the account balance.
    # - account_id: 5–10 alphanumeric characters.
    # - amount: Decimal number between 0.01 and 1,000,000.
    # Errors:
    # - ERROR: Invalid amount.
    # - ERROR: Account not found
    print("deposit")


def withdraw(account_id, amount):
    # TODO:
    #  Subtracts the specified amount from the account balance.
    # - account_id: Must exist.
    # - amount: Decimal number between 0.01 and current account balance.
    # Errors:
    # - ERROR: Invalid amount.
    # - ERROR: Insufficient funds.
    # - ERROR: Account not found.
    print("withdraw")


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
    print("transfer")


def balance(account_id):
    # TODO:
    # Displays the current balance of the specified account.
    # - account_id: Must exist.
    # Errors:
    # - ERROR: Account not found.
    print("balance")


def history(account_id):
    # TODO:
    # Displays the transaction history of the specified account.
    # - account_id: Must exist.
    # Errors:
    # - ERROR: Account not found.
    print("history")


if __name__ == "__main__":
    main()
