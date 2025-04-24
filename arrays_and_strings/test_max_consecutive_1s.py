from unittest import TestCase

from arrays_and_strings.max_consecutive_1s import Solution

class TestSolution(TestCase):
    def test_longest_ones_1(self):
        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        k = 2
        sol = Solution()
        self.assertEqual(sol.longestOnes(nums, k), 6)

    def test_longest_ones_2(self):
        nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
        k = 3
        sol = Solution()
        self.assertEqual(sol.longestOnes(nums, k), 10)
