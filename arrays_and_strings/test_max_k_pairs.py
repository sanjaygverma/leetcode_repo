from unittest import TestCase

from arrays_and_strings.max_k_pairs import Solution

class TestSolution(TestCase):
    def test_max_operations(self):
        sol = Solution()
        nums = [1, 2, 3, 4]
        k = 5
        self.assertEqual(sol.maxOperations(nums, k), 2)

    def test_max_operations_1(self):
        sol = Solution()
        nums = [3, 1, 3, 4, 3]
        k = 6
        self.assertEqual(sol.maxOperations(nums, k), 1)

    def test_max_operations_2(self):
        sol = Solution()
        nums = [3, 5, 1, 5]
        k = 2
        self.assertEqual(sol.maxOperations(nums, k), 0)




