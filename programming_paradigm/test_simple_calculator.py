import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
	def setUp(self):
		self.calc = SimpleCalculator()
	def test_addition(self):
		self.assertEqual(self.calc.add(5,5), 10)
		self.assertEqual(self.calc.add(10,5), 15)
	def test_subtract(self):
		self.assertEqual(self.calc.subtract(10,5), 5)
		self.assertEqual(self.calc.subtract(5,5), 0)
	def test_multiply(self):
		self.assertEqual(self.calc.multiply(2,2), 4)
		self.assertEqual(self.calc.multiply(10, 5), 50)
	def test_divide(self):
		self.assertEqual(self.calc.divide(10,2), 5)
		self.assertEqual(self.calc.divide(5,5), 1)

if __name__ == "__main__":
	unittest.main()
