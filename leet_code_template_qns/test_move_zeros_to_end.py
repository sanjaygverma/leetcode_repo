from unittest import TestCase

from leet_code_template_qns.move_zeros_to_end import Solution

class TestSolution(TestCase):
    def test_move_zeroes_1(self):
        sol = Solution()
        nums = [0,1,0,3,12]
        exp_nums = [1,3,12,0,0]
        sol.moveZeroes(nums)
        self.assertEqual(nums, exp_nums)

    def test_move_zeroes_2(self):
        sol = Solution()
        nums = [0]
        exp_nums = [0]
        sol.moveZeroes(nums)
        self.assertEqual(nums, exp_nums)

    def test_move_zeroes_3(self):
        sol = Solution()
        nums = [0, 0, 0, 0, 0]
        exp_nums = [0, 0, 0, 0, 0]
        sol.moveZeroes(nums)
        self.assertEqual(nums, exp_nums)

    def test_large_list(self):
        nums = [0] * 100 + list(range(1, 101)) + [0] * 100
        Solution().moveZeroes(nums)
        self.assertEqual(nums[:100], list(range(1, 101)))
        self.assertEqual(nums[100:], [0] * 200)




