import unittest
from mpesa import MPESA

class TestMPESA(unittest.TestCase):



	def setUp(self):
        #Gives all test cases access to an instance of the Wallet
		self.mpesa=MPESA() 

	def Test_deposit_cash(self):
		#makes sure the deposut function works well
		self.wallet.balance=0
		self.assertEqual(self.wallet.deposit_cash(1000),1000)
		self.assertEqual(self.wallet.deposit_cash(500),1500)
	def Test_when_deposit_is_too_little(self):
		self.assertEqual(self.wallet.deposit_cash(35),"You cant deposit less than 50 shillings")
if __name__ == '__main__':
	unittest.main()