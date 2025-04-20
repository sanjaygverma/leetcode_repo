#You are given a list of integers. Your task is to write a function find_min(nums), that returns the minimum number
#from the list without using Python's built-in min() function.
#If the list is empty, your function should return None.

from typing import List


class Solution:

    def find_min(self, nums: List[int]) -> int:

        if not nums:
            return None

        left = 0
        right = len(nums) - 1
        mid = len(nums) // 2
        min = nums[left]
        while left <= mid <= right:

            if right == mid or left == 0:
                if nums[right] < min:
                    min = nums[right]
            elif nums[left] < min:
                min = nums[left]
            elif nums[right] < min:
                min = nums[right]

            left += 1
            right -= 1

        return min


if __name__ == '__main__':
    sol = Solution()
    #lst = [-3, -4, -875, -37, -1]
    #lst = [1000000000, 999999999, -999999999, -1000000000]
    #lst = [1, 2, 3, 4, 5]
    #lst = [4, 3, 1, -2, -7]
    #lst = []
    #lst = list(range(100, 0, -1))
    lst = [int(x * x * x - x * x - x) for x in range(1, 101)]
    print(sol.find_min(lst))