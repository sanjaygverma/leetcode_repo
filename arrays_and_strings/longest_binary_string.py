from typing import List

#Find maximum sub array
#longest string having 1s
#TODO - to complete this
class MaxSubArray:

    def find_subarray(self, nums: str) -> str:
        ans = 0
        left = 0
        curr = 0

        var = list()
        #1101100111
        # check if its 0 the change it to 1
        # then check for


        for right in range(len(nums)):

            if nums[right] == 0:
                curr += 1 # increment & track the number of zeros

            while curr > k:
                curr -= nums[left]
                left += 1

            ans = max(ans, right - left + 1)
            if len(nums[left: right + 1]) > len(var):
                var = nums[left: right + 1]

        return var


if __name__ == '__main__':
    msal = MaxSubArray()
    s = '1101100111'
    print(msal.find_subarray(s))
