from __future__ import annotations

import sys
from typing import Any, Dict, List, Optional


class BankSystem:
    def __init__(self) -> None:
        self.users: Dict[str, str] = {}
        self.accounts: Dict[str, Dict[str, Any]] = {}

    # creates a new user with a unique ID and name.
    # - user_id: 5–10 alphanumeric characters.
    # - name: Non-empty string.
    # Errors:
    # - ERROR: User ID already exists.
    # - ERROR: Invalid user ID or name.
    def create_user(self, user_id: str, name: str) -> None:
        if user_id in self.users:
            print("ERROR: User ID already exists.")
        elif not (5 <= len(user_id) <= 10) or not name:
            print("ERROR: Invalid user ID or name.")
            if len(user_id) < 5 or len(user_id) > 10:
                print("User ID length issue:", len(user_id))
                print("Should be between 5 and 10 characters.")
        else:
            self.users[user_id] = name
            print("User created:", user_id, name)

    # Displays user information.
    # - user_id: Must exist.
    # Errors:
    # - ERROR: User not found.
    def read_user(self, user_id: str) -> Optional[str]:
        if user_id in self.users:
            print("User found:", user_id, self.users[user_id])
            return self.users[user_id]
        else:
            print("ERROR: User not found.")
            return None

    # - user_id: Must exist.
    # - new_name: Non-empty string.
    # Errors:
    # - ERROR: User not found.
    # - ERROR: Invalid new name.
    def update_user(self, user_id: str, new_name: str) -> None:
        if user_id in self.users:
            if isinstance(new_name, str) and new_name.strip():
                self.users[user_id] = new_name
                print("User updated:", user_id, new_name)
        else:
            print("ERROR: User not found.")

    # Deletes a user and associated accounts.
    # - user_id: Must exist.
    # Errors:
    # - ERROR: User not found.
    def delete_user(self, user_id: str) -> None:
        if user_id in self.users:
            del self.users[user_id]
            print("User deleted:", user_id)
        else:
            print("ERROR: User not found.")

    ## NOT DESRCRIBED IN SPEC BUT NEEDED FOR TESTS
    # Adds a new bank account for an existing user.
    # - user_id: Must exist.
    # - account_id: 5–10 alphanumeric characters.
    # Errors:
    # - ERROR: User not found.
    # - ERROR: Account ID already exists.
    def add_account(self, user_id: str, account_id: str) -> None:
        if user_id in self.users:
            if account_id not in self.accounts:
                self.accounts[account_id] = {
                    "user_id": user_id,
                    "balance": 0.0,
                    "history": [],
                }
                print("Account added:", account_id)
            else:
                print("ERROR: Account ID already exists.")
        else:
            print("ERROR: User not found.")

    ## NOT DESRCRIBED IN SPEC BUT NEEDED FOR TESTS
    # Removes an existing bank account.
    # - account_id: Must exist.
    # Errors:
    # - ERROR: Account not found.
    def remove_account(self, account_id: str) -> None:
        if account_id in self.accounts:
            del self.accounts[account_id]
            print("Account removed:", account_id)
        else:
            print("ERROR: Account not found.")

    # Adds the specified amount to the account balance.
    # - account_id: 5–10 alphanumeric characters.
    # - amount: Decimal number between 0.01 and 1,000,000.
    # Errors:
    # - ERROR: Invalid amount.
    # - ERROR: Account not found
    def deposit(self, account_id: str, amount: str) -> None:
        if account_id in self.accounts:
                amt = float(amount)
                if 0.01 <= amt <= 1000000:
                    self.accounts[account_id]["balance"] += amt
                    self.accounts[account_id]["history"].append(f"Deposited: {amt}")
                    print(
                        f"Deposited {amt} to account {account_id}. New balance: {self.accounts[account_id]['balance']}"
                    )
                else:
                    print("ERROR: Invalid amount.")
        else:
            print("ERROR: Account not found")

    # Displays the current balance of the specified account.
    # - account_id: Must exist.
    # Errors:
    # - ERROR: Account not found.
    def balance(self, account_id: str) -> float | None:
        if account_id in self.accounts:
            bal = float(self.accounts[account_id]["balance"])
            print(f"Account {account_id} balance: {bal}")
            return bal
        else:
            print("ERROR: Account not found.")
            return None

    # Displays the transaction history of the specified account.
    # - account_id: Must exist.
    # Errors:
    # - ERROR: Account not found.
    def history(self, account_id: str) -> Optional[List[str]]:
        if account_id in self.accounts:
            hist = list(self.accounts[account_id]["history"])
            print(f"Account {account_id} history: {hist}")
            return hist
        else:
            print("ERROR: Account not found")
            return None

    #  Subtracts the specified amount from the account balance.
    # - account_id: Must exist.
    # - amount: Decimal number between 0.01 and current account balance.
    # Errors:
    # - ERROR: Invalid amount.
    # - ERROR: Insufficient funds.
    # - ERROR: Account not found.
    def withdraw(self, account_id: str, amount: str) -> None:
        if account_id in self.accounts:
            amt = float(amount)
            bal = self.balance(account_id)
            if bal is not None and 0.01 <= amt <= bal:
                self.accounts[account_id]["balance"] -= amt
                self.accounts[account_id]["history"].append(f"Withdraw: {amt}")
                print(
                    f"Withdrew {amt} from account {account_id}. New balance: {self.accounts[account_id]['balance']}"
                )
            else:
                if bal is not None and amt > bal:
                    print("ERROR: insufficient funds.")
                if amt < 0.01:
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
    def transfer(self, source_id: str, dest_id: str, amount: str) -> None:
        if source_id == dest_id:
            print("ERROR: Source and destination cannot be the same.")
            return

        # Validate accounts exist
        if source_id not in self.accounts:
            print("ERROR: Account not found.")
            return
        if dest_id not in self.accounts:
            print("ERROR: Destination account not found.")
            return

        # Validate amount
        amt = float(amount)
        if not (0.01 <= amt <= 1000000):
            print("ERROR: Invalid amount.")
            return

        # Check funds
        source_balance = float(self.accounts[source_id]["balance"])
        if amt > source_balance:
            print("ERROR: Insufficient funds.")
            return

        # Perform transfer atomically on stored balances/history
        self.accounts[source_id]["balance"] -= amt
        self.accounts[source_id]["history"].append(f"Withdraw: {amt}")
        self.accounts[dest_id]["balance"] += amt
        self.accounts[dest_id]["history"].append(f"Deposited: {amt}")
        print(
            f"Transferred {amt} from account {source_id} to {dest_id}. "
            f"New balances: {source_id}: {self.accounts[source_id]['balance']}, "
            f"{dest_id}: {self.accounts[dest_id]['balance']}"
        )

    ## Parses the input file and executes commands line by line
    # Function for processing input commands from a file
    def process_file(self, filename: str) -> None:
        try:
            with open(filename, "r+") as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Error opening {filename}: {e}", file=sys.stderr)
            sys.exit(1)

        for line in lines:
            line_to_process = line.strip()
            # if not line_to_process:
            #     continue
            parts = line_to_process.split()
            cmd = parts[0]
            args = parts[1:]

            if cmd == "help":
                self.print_help()
            elif cmd == "create_user" and len(args) >= 2:
                self.create_user(args[0], args[1])
            elif cmd == "read_user" and len(args) >= 1:
                self.read_user(args[0])
            elif cmd == "update_user":
                # print("args[1]:", args[1])
                if len(args) < 2:
                    print("ERROR: Invalid new name. Cant be empty")
                    continue
                elif len(args) >= 2:
                    self.update_user(args[0], args[1])
            elif cmd == "delete_user" and len(args) >= 1:
                self.delete_user(args[0])
            elif cmd == "deposit" and len(args) >= 2:
                self.deposit(args[0], args[1])
            elif cmd == "withdraw" and len(args) >= 2:
                self.withdraw(args[0], args[1])
            elif cmd == "transfer" and len(args) >= 3:
                self.transfer(args[0], args[1], args[2])
            elif cmd == "balance" and len(args) >= 1:
                self.balance(args[0])
            elif cmd == "history" and len(args) >= 1:
                self.history(args[0])
            elif cmd == "add_account" and len(args) >= 2:
                self.add_account(args[0], args[1])
            elif cmd == "remove_account" and len(args) >= 1:
                self.remove_account(args[0])
            elif cmd == "clear_bank":
                self.clear_bank()
            else:
                print(f"Unknown or malformed command: {line_to_process}")

    # Displays a list of available commands and their descriptions
    def print_help(self) -> None:
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

    ##FOR TESTING
    # Removes everyting in storage
    def clear_bank(self) -> None:
        self.users: Dict[str, str] = {}
        self.accounts: Dict[str, Dict[str, Any]] = {}


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python3 object_main.py <file.txt>", file=sys.stderr)
        return 1

    filename = sys.argv[1]
    system = BankSystem()
    system.process_file(filename)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
