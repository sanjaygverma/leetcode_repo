from unittest import TestCase

#TODO check
class TestSolution(TestCase):
    def test_find_min(self):
        self.fail()
'''
import unittest
from typing import List, Union
from solution import find_min

class TestFindMin(unittest.TestCase):
    def test1(self):
        self.assertEqual(find_min([1, 2, 3, 4, 5]), 1)

    def test2(self):
        self.assertEqual(find_min([]), None)

    def test3(self):
        self.assertEqual(find_min([4, 3, 1, -2, -7]), -7)

    def test4(self):
        self.assertEqual(find_min([100, 100, 100, 100]), 100)

    def test5(self):
        self.assertEqual(find_min([-3, -4, -875, -37, -1]), -875)

    def test6(self):
        self.assertEqual(find_min([0, 90, 35]), 0)

    def test7(self):
        self.assertEqual(find_min([1000000000, 999999999, -999999999, -1000000000]), -1000000000)

    def test8(self):
        self.assertEqual(find_min(list(range(100, 0, -1))), 1)

    def test9(self):
        self.assertEqual(find_min([int(x * x * x - x * x - x) for x in range(1, 101)]), -1)

    def test10(self):
        self.assertEqual(find_min([0]), 0)


if __name__ == '__main__':
    unittest.main()
'''