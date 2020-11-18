import unittest
from testcase_py import addproduct

from ddt import ddt,data,unpack

@data
class MainFrame(unittest.TestCase):

	def setUp(self):
		print("begin")

	def test_01(self):
		a1 = addproduct.AddProduct()
		a1.addProduct()







	def tearDown(self):
		print("finished!")

if __name__ == '__main__':
    unittest.main()