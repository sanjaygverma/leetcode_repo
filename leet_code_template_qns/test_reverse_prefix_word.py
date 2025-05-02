from unittest import TestCase

from leet_code_template_qns.reverse_prefix_word import Solution

class TestSolution(TestCase):
    def test_reverse_prefix_1(self):
        sol = Solution()
        self.assertEqual("dcbaefd", sol.reversePrefix("abcdefd", "d"))


