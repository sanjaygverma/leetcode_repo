from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = curr = ans = 0
        for i in range(len(nums)):
            curr += nums[i] #5  i-2


            # nums = [2,3,1,2,4,3]
            # nums = [1,4,4]

            while curr >= target:
                if left == 0:
                    ans = i - left + 1 #1-1+1 - 1
                else:
                    ans = min(ans, i - left + 1)
                curr -= nums[left] #4
                left += 1 #left -> 2

        return ans

