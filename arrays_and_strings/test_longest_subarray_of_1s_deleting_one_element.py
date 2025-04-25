from unittest import TestCase

from arrays_and_strings.longest_subarray_of_1s_deleting_one_element import Solution

class TestSolution(TestCase):
    def test_longest_subarray(self):
        sol = Solution()
        nums = [0,1,1,1,0,1,1,0,1]
        self.assertEqual(sol.longestSubarray(nums), 5)
