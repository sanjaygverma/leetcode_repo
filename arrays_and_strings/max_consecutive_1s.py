# Given a binary array nums and an integer k,
# return the maximum number of
# consecutive 1's in the array if you can flip at most k 0's.
#
#
# Example 1:
#
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:
#
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length

from typing import List


# Approach : Dynamic Sliding window
#
# Define the window with two pointers ( start and end pointers ) which are
# initially pointing to zero index of the array.
# If you encounter 1 while traversing the list increase the size of window
# by increasing the end_pointer by 1.
# If you encounter 0 and your k > 0 then keep on increasing the size of window by increasing end_pointer by 1.
# Decrease the k by 1 to account for that you encountered 0
# If your k becomes 0 in this process then remove the earliest zero in the window and move the start pointer
# to index of earliest zero +1
# Don't forget to keep track of the length of the sequence in this process.
# Hope it helps and don't get disheartened ( it will take time )

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flp_ctr = k
        mx_1s_ctr = l_ptr = 0
        for r_ptr in range(len(nums)):
            if nums[r_ptr] == 0:
                flp_ctr -= 1
            while flp_ctr < 0: # exceeds k, so reset flp_ctr and move the left pointer of window to first 0
                if nums[l_ptr] == 0:
                    flp_ctr += 1
                l_ptr += 1
            mx_1s_ctr = max(mx_1s_ctr, (r_ptr - l_ptr) +1)
        return mx_1s_ctr
