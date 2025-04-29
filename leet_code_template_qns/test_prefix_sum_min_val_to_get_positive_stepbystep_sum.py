from unittest import TestCase

from leet_code_template_qns.prefix_sum_min_val_to_get_positive_stepbystep_sum import Solution

class TestSolution(TestCase):
    def test_min_start_value_1(self):
        sol = Solution()
        nums = [1, -2, -3]
        self.assertEqual(5, sol.minStartValue(nums))

    def test_min_start_value_2(self):
        sol = Solution()
        nums = [-3,2,-3,4,2]
        self.assertEqual(5, sol.minStartValue(nums))


    def test_min_start_value_3(self):
        sol = Solution()
        nums = [2,3,5,-5,-1] #
        self.assertEqual(1, sol.minStartValue(nums))