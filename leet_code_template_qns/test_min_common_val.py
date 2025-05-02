from unittest import TestCase
from leet_code_template_qns.min_common_val import Solution

class TestSolution(TestCase):
    def test_get_common_1(self):
        sol = Solution()
        nums1 = [1,2,3]
        nums2 = [2,4]
        self.assertEqual(2, sol.getCommon(nums1, nums2))

    def test_get_common_2(self):
        sol = Solution()
        nums1 = [1,2,3,6]
        nums2 = [2,3,4,5]
        self.assertEqual(2, sol.getCommon(nums1, nums2))

    def test_get_common_3(self):
        sol = Solution()
        nums1 = [1,2,3,6]
        nums2 = [4,5]
        self.assertEqual(-1, sol.getCommon(nums1, nums2))
