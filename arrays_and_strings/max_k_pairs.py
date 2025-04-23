# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and
# remove them from the array.
# Return the maximum number of operations you can perform on the array.
from typing import List


class Solution:

    def maxOperations(self, nums: List[int], k: int) -> int:

        if len(nums) == 0 or len(nums) == 1:
            return 0

        l = 0
        r = len(nums) - 1
        cnt = 0
        #d = dict()
        nums.sort()


        while l < r:

            if nums[l] + nums[r] == k:
                cnt += 1
                r -= 1
                l += 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                r -= 1
        return cnt
