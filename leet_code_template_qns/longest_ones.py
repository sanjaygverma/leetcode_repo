from typing import List


class Solution:

    def longestOnes(self, nums: List[int], k: int) -> int:
        left = ans = 0
        k_cntr = 0

        for right in range(len(nums)):
            # do logic here to add arr[right] to curr

            if nums[right] == 0:
                k_cntr += 1

            while k_cntr > k:
                # remove arr[left] from curr
                if nums[left] == 0:
                    k_cntr -= 1
                left += 1

            ans = max(ans, (right - left) + 1)
            # update ans
        return ans
