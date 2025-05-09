from unittest import TestCase

from leet_code_template_qns.min_size_sub_arr import Solution

class TestSolution(TestCase):
    def test_min_sub_array_len_1(self):
        nums = [2,3,1,2,4,3]
        tgt = 7
        sol = Solution()
        self.assertEqual(2, sol.minSubArrayLen(tgt, nums))

    #nums = [1,4,4]
    def test_min_sub_array_len_2(self):
        nums = [1,4,4]
        tgt = 1
        sol = Solution()
        self.assertEqual(1, sol.minSubArrayLen(tgt, nums))

    def test_min_sub_array_len_3(self):
        nums = [1,1,1,1,1,1,1,1]
        tgt = 11
        sol = Solution()
        self.assertEqual(0, sol.minSubArrayLen(tgt, nums))

