# You are given an array of integers.
# Your job is to return the count of even and odd integers in the given array
# without using any built-in Python methods.
# Your function should return a tuple in the format (even_count, odd_count),
# where even_count represents the number of even integers and odd_count
# represents the number of odd integers in the provided array.
from typing import List, Tuple


class Solution:

    def solution(self, nums: List[int]) -> Tuple[int]:

        left = 0
        right = len(nums) - 1
        mid = len(nums) // 2

        evenCnt = 0
        oddCnt = 0
        while left <= mid <= right:

            if left < mid:
                if nums[left] == 0 or nums[left] % 2 == 0:
                    evenCnt += 1
                else:
                    oddCnt += 1

            if nums[right] == 1 or not nums[right] % 2 == 0:
                oddCnt += 1
            else:
                evenCnt += 1

            left += 1
            right -= 1

        tup = tuple([evenCnt, oddCnt])
        return tup

if __name__ == '__main__':
    sol = Solution()
    #ls = [1, 2, 3, 4, 5]
    #ls = [1]
    #ls = [-2]
    #ls = [1, -2, 3, -4, 5, -6, 7]
    #ls = [0]
    #ls = [0, 0, 0, 0, 0]
    #ls = list(range(-1000, 1001))
    #ls = []
    ls = [-3, -2, -1, 0, 1, 2, 3]
    print(sol.solution(ls))
