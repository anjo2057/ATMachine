import unittest

from object_main import BankSystem

class TestMain(unittest.TestCase):


    ## TC001
    # Testing adding of users and all ERRORS
    def test_create_user(self):
        bank = BankSystem()

        #for valid user
        bank.create_user("U0001", "Alice")
        self.assertIn("U0001", bank.users)
        self.assertEqual(bank.users["U0001"], "Alice")

        #For unvalid user
        bank.create_user("U01", "Bob")  
        self.assertNotIn("U01", bank.users) 

        #For adding of already excisting user_id
        bank.create_user("U0001", "knutte")
        self.assertNotIn("knutte", bank.users["U0001"])

        # Clearing all inputs for next test
        bank.clear_bank()
    
    ## TC0002
    # Testing reading user
    def test_read_user(self):
        bank = BankSystem()

        bank.create_user("U0001", "Alice")
        self.assertIn("U0001", bank.users)
        self.assertEqual(bank.users["U0001"], "Alice")
        
        #For valid reading of a user
        self.assertEqual(bank.read_user("U0001"), "Alice")

        #For unvlaid reading users.
        self.assertIsNone(bank.read_user("U0002"))

        bank.clear_bank() 

    ## TC0003
    # Testing updating user
    def test_update_user(self):
        bank = BankSystem() 

        bank.create_user("U0001", "Alice")
        self.assertIn("U0001", bank.users)
        self.assertEqual(bank.users["U0001"], "Alice")

        #For valid updating of a user
        bank.update_user("U0001", "Alicia")
        self.assertEqual(bank.users["U0001"], "Alicia")

        #For unvlaid updating users.
        bank.update_user("U0002", "Bille")
        self.assertNotIn("U0002", bank.users)

        #For invalid new name
        bank.update_user("U0001", "")
        self.assertEqual(bank.users["U0001"], "Alicia") 

        bank.clear_bank()


    ## TC0004
    # Testing deleting user
    def test_delete_user(self):
        bank = BankSystem() 

        bank.create_user("U0001", "Alice")
        self.assertIn("U0001", bank.users)
        self.assertEqual(bank.users["U0001"], "Alice")

        #For valid deleting of a user
        bank.delete_user("U0001")
        self.assertNotIn("U0001", bank.users)

        #For unvlaid deleting users.
        bank.delete_user("U0002")  
        self.assertNotIn("U0002", bank.users)

        bank.clear_bank()

    ## TC0005
    # Testing depositing money to account
    def test_deposit(self):
        bank = BankSystem() 

        bank.create_user("U0001", "Alice")
        bank.add_account("U0001", "AC001")

        #For valid deposit
        bank.deposit("AC001", "500")
        self.assertEqual(bank.accounts["AC001"]["balance"], 500)

        #For invalid deposit (negative amount)
        bank.add_account("U0001", "AC002")
        bank.deposit("AC002", "-100")
        self.assertEqual(bank.accounts["AC002"]["balance"], 0) 

        #For invalid deposit (non-existing account)
        bank.deposit("A002", "200")
        self.assertNotIn("A002", bank.accounts) 

        bank.clear_bank()

    ## TC0006
    # Testing checking balance of account
    def test_balance(self):
        bank = BankSystem() 

        bank.create_user("U0001", "Alice")
        bank.add_account("U0001", "AC001")
        bank.deposit("AC001", "500")

        #For valid balance check
        balance = bank.balance("AC001")
        self.assertEqual(balance, 500)

        #For invalid balance check (non-existing account)
        balance = bank.balance("AC002")
        self.assertIsNone(balance) 

        bank.clear_bank()


    ## TC0007
    # Testing history of account
    def test_history(self):
        bank = BankSystem() 

        bank.create_user("U0001", "Alice")
        bank.add_account("U0001", "AC001")
        bank.deposit("AC001", "500")
        bank.withdraw("AC001", "200")

        #For valid history check
        history = bank.history("AC001")
        assert history is not None
        self.assertIn("Deposited: 500.0", history)
        self.assertIn("Withdraw: 200.0", history)

        #For invalid history check (non-existing account)
        history = bank.history("AC002")
        self.assertIsNone(history) 

        bank.clear_bank()

    ## TC0008
    # Testing withdrawing money from account
    def test_withdraw(self):
        bank = BankSystem() 

        bank.create_user("U0001", "Alice")
        bank.add_account("U0001", "AC001")
        bank.deposit("AC001", "500")

        #For valid withdraw
        bank.withdraw("AC001", "200")
        self.assertEqual(bank.accounts["AC001"]["balance"], 300)

        #For invalid withdraw (exceeding balance)
        bank.withdraw("AC001", "400")
        self.assertEqual(bank.accounts["AC001"]["balance"], 300) 

        #For invalid withdraw (non-existing account)
        bank.withdraw("AC002", "100")
        self.assertNotIn("AC002", bank.accounts) 

        #For invalid withdraw (negative amount)
        bank.withdraw("AC001", "-400")
        self.assertEqual(bank.accounts["AC001"]["balance"], 300)

        bank.clear_bank()
    
    ## TC0009
    # Testing transferring money between accounts
    def test_transfer(self):
        bank = BankSystem() 

        bank.create_user("U0001", "Alice")
        bank.add_account("U0001", "AC001")
        bank.add_account("U0001", "AC002")
        bank.deposit("AC001", "500")

        #For valid transfer
        bank.transfer("AC001", "AC002", "200")
        self.assertEqual(bank.accounts["AC001"]["balance"], 300)
        self.assertEqual(bank.accounts["AC002"]["balance"], 200)

        #For invalid transfer (exceeding balance)
        bank.transfer("AC001", "AC002", "400")
        self.assertEqual(bank.accounts["AC001"]["balance"], 300) 
        self.assertEqual(bank.accounts["AC002"]["balance"], 200) 

        #For invalid transfer (non-existing sourceaccount)
        bank.transfer("AC003", "AC002", "100")
        self.assertNotIn("AC003", bank.accounts) 

        #For invalid transfer (non-existing destination account)
        bank.transfer("AC002", "AC003", "100")
        self.assertNotIn("AC003", bank.accounts) 

        #For invalid transfer (same account)
        bank.transfer("AC001", "AC001", "100")
        self.assertEqual(bank.accounts["AC001"]["balance"], 300)

        bank.clear_bank()

    def test_help(self): 
        bank = BankSystem() 
        # Just to see that help runs without errors
        bank.print_help()
        bank.clear_bank()

    


if __name__ == "__main__":
     unittest.main()