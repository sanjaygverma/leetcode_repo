from typing import List
from typing import List

import math


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        lp = 0
        maxp = len(nums) - 1

        # idx_ls = [x for x in range(len(nums))]
        ret_lst = list()

        product_of_all = math.prod(nums)
        product_of_all_no_zero = 1

        if nums.count(0) > 1:
            product_of_all_no_zero = 0
        else:
            l = [x for x in nums if x != 0]
            if len(l) > 0:
                product_of_all_no_zero = math.prod(l)



        while lp <= maxp:

            # ils = list(idx_ls)
            # del ils[lp]

            # for i in ils:
            #    prdt = prdt * nums[i]

            if not nums[lp] == 0:
                prdt = int(product_of_all) / nums[lp]
            else:
                prdt = product_of_all_no_zero

            ret_lst.append(int(prdt))

            lp += 1

        return ret_lst








if __name__ == '__main__':
    sol = Solution()
    ls = [0,0]
    print(sol.productExceptSelf(ls))





