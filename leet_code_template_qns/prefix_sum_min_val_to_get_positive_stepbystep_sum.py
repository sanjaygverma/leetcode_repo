from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        prefix = [nums[0]]

        for right in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[right])
        min_val = min(prefix)

        if min_val < 0:
            if abs(min_val) + 1 - abs(min_val) == 1:
                min_val = abs(min_val) + 1
        else:
            if min_val + 1 - min_val == 1:
                min_val = min_val + 1

        return min_val
