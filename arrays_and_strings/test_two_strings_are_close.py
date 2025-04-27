from unittest import TestCase

from arrays_and_strings.two_strings_are_close import Solution

class TestSolution(TestCase):
    def test_close_strings_1(self):
        sol = Solution()
        self.assertEqual(sol.closeStrings("abc", "abc"), True)

    def test_close_strings_2(self):
        sol = Solution()
        self.assertEqual(sol.closeStrings("a", "aa"), False)

    def test_close_strings_3(self):
        sol = Solution()
        self.assertEqual(sol.closeStrings("cabbba", "abbccc"), False)

    def test_close_strings_4(self):
        sol = Solution()
        self.assertEqual(sol.closeStrings("abbzccca", "babzzczc"), True)

    def test_close_strings_5(self):
        sol = Solution()
        self.assertEqual(sol.closeStrings("abbzzca", "babzzcz"), False)