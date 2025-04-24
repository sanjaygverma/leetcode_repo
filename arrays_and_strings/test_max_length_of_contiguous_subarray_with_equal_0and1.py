from unittest import TestCase

from arrays_and_strings.max_length_of_contiguous_subarray_with_equal_0and1 import Solution

class TestSolution(TestCase):
    def test_find_max_length(self):
        sol = Solution()
        #nums = [0,1]
        nums = [0, 1, 1, 0, 1, 1]
        self.assertEqual(sol.findMaxLength(nums), 2)
