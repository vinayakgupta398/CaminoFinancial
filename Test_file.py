Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import unittest
>>> from Customers import Customer
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    from Customers import Customer
ImportError: No module named 'Customers'
>>> from Customers import Customer
class Test(unittest.TestCase):
  def check_balance(self):
    customer1=Customer()
    customer1.__init__('Vinayak')
    customer1.set_balance('1000')
    self.assertTrue(true)
    self.assertTrue(true)
    self.assertTrue(customer1.deposit('500'),'Deposit successful')
    self.assertTrue(customer1.withdraw('200'),'The withdrawl is possible')
if __name__='__main__':
  unittest.main()
  
  
    
