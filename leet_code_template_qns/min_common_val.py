from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        nums1_len = len(nums1)
        nums2_len = len(nums2)

        i = j = 0
        ret_val = -1
        while i < nums1_len and j < nums2_len:

            if nums1[i] == nums2[j]:
                ret_val = nums1[i]
                break
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return ret_val
