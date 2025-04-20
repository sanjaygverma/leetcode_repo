from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqrd = [ e * e for e in nums]
        sqrd.sort()
        return sqrd
