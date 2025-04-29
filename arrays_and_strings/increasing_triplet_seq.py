from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        isTriplet = False

        a = java_int_max = (1 << 31) - 1
        b = java_int_max = (1 << 31) - 1

        for num in nums:

            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                isTriplet = True

        return isTriplet


if __name__ == '__main__':
    sol = Solution()
    #n = [1,2,3,4,5]
    #n = [5, 4, 3, 2, 1]
    n = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    print(sol.increasingTriplet(n))