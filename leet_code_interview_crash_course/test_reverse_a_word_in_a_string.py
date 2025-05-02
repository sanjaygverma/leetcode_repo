from unittest import TestCase

from leet_code_interview_crash_course.reverse_a_word_in_a_string import Solution

class TestSolution(TestCase):
    def test_reverse_words(self):
        s = "Let's take LeetCode contest"
        sol = Solution()
        self.assertEqual("s'teL ekat edoCteeL tsetnoc", sol.reverseWords(s))
