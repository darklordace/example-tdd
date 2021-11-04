import unittest
from app import foo

class TestFoo(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(foo(2, 3), 6, "2 x 3 should be 6")
        
    def test_case_2(self):
        self.assertEqual(foo(5, 10), 50, "5 x 10 should be 50")
        
    def test_case_3(self):
        self.assertEqual(foo(-2, 20), -40, "-2 x 20 should be -40")

if __name__ == '__main__':
    unittest.main()
