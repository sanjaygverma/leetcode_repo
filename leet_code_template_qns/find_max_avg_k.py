from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        left = ans = curr = 0
        cntr = 0

        if len(nums) == 1 and k == 1:
            return nums[0]/k

        for right in range(len(nums)):
            curr += nums[right]
            cntr += 1

            while cntr == k:
                avg = curr / k
                if (ans == 0):
                    ans = avg
                else:
                    ans = max(ans, avg)
                curr = curr - nums[left]
                cntr -= 1
                left += 1
        return round(ans, 5)





