from typing import List

#Find maximum sub array
#sliding window two pointer
class MaxSubArray:

    def find_subarray(self, nums: List[int], k: int) -> List[int]:
        ans = 0
        left = 0
        curr = 0

        var = list()

        for right in range(len(nums)):

            curr += nums[right]

            while curr > k:
                curr -= nums[left]
                left += 1

            ans = max(ans, right - left + 1)
            if len(nums[left: right + 1]) > len(var):
                var = nums[left: right + 1]

        return var


if __name__ == '__main__':
    msal = MaxSubArray()
    ls = [3, 1, 2, 7, 4, 2, 1, 1, 5]
    print(msal.find_subarray(ls, 8))
