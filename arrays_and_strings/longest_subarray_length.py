from typing import List

# Uses two pointer, sliding window technique to retrieve the max sub array length.
# Also check, longest_subarray.py for subarray

class MaxSubArrayLength:

    def find_length(self, nums: List[int], k :int) -> int:
        ans = 0
        left = 0
        curr = 0

        for right in range(len(nums)):
            curr += nums[right]

            while curr > k:
                curr -= nums[left]
                left += 1

            ans = max(ans, right - left + 1)
        return ans

if __name__ == '__main__':
    msal = MaxSubArrayLength()
    ls = [3, 1, 2, 7, 4, 2, 1, 1, 5]
    print(msal.find_length(ls, 8))
