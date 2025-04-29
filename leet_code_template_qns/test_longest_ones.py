from unittest import TestCase

from leet_code_template_qns.longest_ones import Solution


class TestSolution(TestCase):
    def test_longest_ones_1(self):
        sol = Solution()
        nums = [1,1,1,0,0,0,1,1,1,1,0]
        k = 2
        self.assertEqual(6, sol.longestOnes(nums, k))
