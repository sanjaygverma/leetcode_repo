from unittest import TestCase
from arrays_and_strings.equal_row_col_pairs import Solution

class TestSolution(TestCase):
    def test_equal_pairs_1(self):
        sol = Solution()
        grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
        self.assertEqual(sol.equalPairs(grid), 1)

    def test_equal_pairs_2(self):
        sol = Solution()
        grid = [[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]
        self.assertEqual(sol.equalPairs(grid), 3)



