from typing import List
#
# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
#
#
#
# Example 1:
#
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:
#
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Example 3:
#
# Input: nums = [0,1,1,1,1,1,0,0,0]
# Output: 6
# Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        dictnary = {}
        zero_ones_cntr = 0
        max_len = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                zero_ones_cntr -= 1
            else:
                zero_ones_cntr +=1

            if zero_ones_cntr == 0:
                max_len = i+1

            if zero_ones_cntr in dictnary:
                max_len = max(max_len, i - dictnary[zero_ones_cntr])
            else:
                dictnary[zero_ones_cntr] = i

        return max_len