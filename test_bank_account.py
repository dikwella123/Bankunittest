import unittest

from bank_account import BankAccount, MinimumBalanceAccount

class AccountBalanceTestCase(unittest.TestCase):
    def setUp(self):
        self.myAccount = BankAccount()

    def test_balance(self):
        self.assertEqual(self.myAccount.balance, 3000, msg='Account Balance Invalid.')
    def test_deposit(self):
        self.myAccount.deposit(4000)
        self.assertEqual(self.myAccount.balance, 7000, msg='Deposit Method not acurate!')

    def test_withdraw(self):
        self.myAccount.withdraw(500)
        self.assertEqual(self.myAccount.balance, 2500, msg='Withdraw method not accurate')

    def test_invalid_transaction(self):
        self.assertEqual(self.myAccount.withdraw(6000), "Invalid Transaction", msg='Invalid Transaction')
        #self.assertEqual(self.myAccount.withdraw(10000), "Invalid Transaction", msg='Invalid Transaction.' )

    def test_sub_class(self):
        self.assertTrue(issubclass(MinimumBalanceAccount, BankAccount), msg='Not a true subclass of Balance Account.')


         


         