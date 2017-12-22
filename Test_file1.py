import unittest
from Customers import Customer


class test_bank(unittest.TestCase):
	def setUp(self):
		#creating the user before every single test
		Customer('Vinayak')
		#assigning the user a balance before every single test
		Customer.set_balance(self,1000)
		
	def tearDown(self):
		pass

	def test_withdraw(self):
		#Customer('Vinayak')
		#self.Customer.set_balance(self,1000)
		amount_bank = Customer.withdraw(self,200)
		self.assertEqual(amount_bank,800)
		#self.assertEqual(true)

	def test_deposit(self):
		amount_bank=Customer.deposit(self,500)
		#print(amount_bank)
		self.assertEqual(amount_bank,1500)

if __name__ == '__main__':
	unittest.main()

