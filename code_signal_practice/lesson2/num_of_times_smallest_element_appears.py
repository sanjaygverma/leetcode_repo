# You are given an array of integers. Your task is to write a function in Python that returns the number of times the
# smallest element appears in the array.
# Please note that built-in methods such as min() or count() should not be used in this task.
# Your goal is to accomplish this task by iterating over the array elements manually.
# Try to solve the task by doing just a single list traversal.
from typing import List


class SmallestElementArray:

    def count_min(self, numbers: List[int]) -> int:
        # TODO: Implement this function to count the smallest integer in the list.

        if 1 == len(numbers):
            return 1

        if len(numbers) == 0:
            return 0


        left = 0
        right = len(numbers) - 1
        mid = len(numbers) // 2
        min = numbers[left]
        minCnt = 0
        idx_left_zero_passed = False

        while left <= mid <= right:


            if left == 0:
                idx_left_zero_passed = True
                if numbers[right] < min:
                    min = numbers[right]
                    minCnt = 1
                elif numbers[right] == min:
                    minCnt += 1
            else:
                rtVal = numbers[right]
                lVal = numbers[left]

                if rtVal < min:
                    min = rtVal
                    minCnt = 1
                elif rtVal == min:
                    minCnt += 1

                if lVal < min:
                    min = lVal
                    minCnt = 1
                elif lVal == min:
                    minCnt += 1


            # 1

            '''if left < mid and  idx_left_zero_passed :
                if numbers[left] < numbers[right]:
                    if numbers[left] < min:
                        min = numbers[left]
                        minCnt = 1
                    elif numbers[left] == min:
                        minCnt += 1
                    else:
                        min = numbers[right]
                        minCnt = 1
                elif numbers[left] == numbers[right]:
                    minCnt += 1'''

            # 2
            '''if right == mid:
                if numbers[right] < min:
                    min = numbers[right]
                    minCnt = 1
                elif numbers[right] == min:
                    minCnt += 1'''

            # 3



            left += 1
            right -= 1

        t = set(numbers)
        if len(t) == 1:
            minCnt += 1

        return minCnt


if __name__ == '__main__':
    sol = SmallestElementArray()
    #ls = [2, 3, 4, 2, 1, 1, 5]
    #ls = [-3, -1, -1, -3, -5, -2, -3]
    #ls = [1]

    #ls = [-100, -100, -99, 0, 100]
    #ls = [99]*50 + [100]*50
    #ls = list(range(-100, 101))

    #ls = [5, 5, 5, 5]
    #ls = []

    minCt = sol.count_min(ls)
    print(minCt)
