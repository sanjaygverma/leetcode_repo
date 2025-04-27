from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        # eg 1 -
        # grid = [[3,2,1],[1,7,6],[2,7,7]]
        # 1 equal row and column pair

        # constraint - row len and col len are same
        # row 2 and col 1
        # elements of the list

        # row 2 attributes
        # grid[2][0]
        # grid[2][1]
        # grid[2][2]

        # col 1
        # grid[0][1]
        # grid[1][1]
        # grid[2][1]

        # iteration happens
        #  0[0], 1 ,2
        #  1[0], 1, 2

        n_col_cntr = len(grid)
        ret_cnt = 0
        for i in range(len(grid)):
            lst_row = grid[i]

            col_cntr = 0  # tracks cnt of all cols iteration to grid[i] len
            lst_col = list()

            for j in range(len(grid[i])):

                while col_cntr < n_col_cntr:
                    lst_col.append(grid[col_cntr][j])
                    col_cntr += 1

                if lst_row == lst_col:
                    ret_cnt += 1
                col_cntr = 0
                lst_col.clear()

        return ret_cnt