import unittest

from object_main import BankSystem

class TestMain(unittest.TestCase):


    ##Testing adding of users
    def test_create_user(self):
        bank = BankSystem()
        bank.create_user("U0001", "Alice")
        self.assertIn("U0001", bank.users)
        self.assertEqual(bank.users["U0001"], "Alice")
    