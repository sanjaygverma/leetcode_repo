from unittest import TestCase
from code_signal_practice.find_vowels_posns import FindVowelPosns

class TestFindVowelPosns(TestCase):

    def test_solution(self):
        fvp = FindVowelPosns()
        self.assertEqual(fvp.solution("hello"), [1, 4])

    def test2(self):
        fvp = FindVowelPosns()
        self.assertEqual(fvp.solution("HEY"), [1])

    def test3(self):
        fvp = FindVowelPosns()
        self.assertEqual(fvp.solution("hEllOworLd"), [1, 4, 6])

    def test4(self):
        fvp = FindVowelPosns()
        self.assertEqual(fvp.solution("xyzxyz"), [])

    def test5(self):
        fvp = FindVowelPosns()
        self.assertEqual(fvp.solution("aeiou"), [0, 1, 2, 3, 4])

    def test6(self):
        fvp = FindVowelPosns()
        self.assertEqual(fvp.solution("AEIOUAEIOUaeiouaeiou"),
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])

    def test7(self):
        fvp = FindVowelPosns()
        self.assertEqual(fvp.solution("a" * 500), list(range(500)))

    def test8(self):
        fvp = FindVowelPosns()
        self.assertEqual(fvp.solution("b" * 500), [])

    def test9(self):
        fvp = FindVowelPosns()
        self.assertEqual(fvp.solution("C" * 250 + "aeiou" * 50), list(range(250, 500)))

    def test10(self):
        fvp = FindVowelPosns()
        self.assertEqual(fvp.solution("a" * 250 + "b" * 250), list(range(250)))
