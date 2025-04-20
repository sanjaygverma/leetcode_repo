from unittest import TestCase
from code_signal_practice.shift_letter_in_alphabetical_order import ShiftAlphabetOrder

class TestShiftAlphabetOrder(TestCase):
    def test_solution(self):
        sao = ShiftAlphabetOrder()
        self.assertEqual(sao.solution('abc123XYz!'), 'bcd123YZa!')

    def test1(self):
        sao = ShiftAlphabetOrder()
        self.assertEqual(sao.solution("abc123XYz!"), "bcd123YZa!")

    def test2(self):
        sao = ShiftAlphabetOrder()
        self.assertEqual(sao.solution("Hello, World!"), "Ifmmp, Xpsme!")

    def test3(self):
        sao = ShiftAlphabetOrder()
        self.assertEqual(sao.solution("9876543210"), "9876543210")

    def test4(self):
        sao = ShiftAlphabetOrder()
        self.assertEqual(sao.solution("nhpq$%EPV45JZ"), "oiqr$%FQW45KA")

    def test5(self):
        sao = ShiftAlphabetOrder()
        self.assertEqual(sao.solution("Pythoniscool"), "Qzuipojtdppm")

    def test6(self):
        sao = ShiftAlphabetOrder()
        self.assertEqual(sao.solution("Zebra"), "Afcsb")

    def test7(self):
        sao = ShiftAlphabetOrder()
        self.assertEqual(sao.solution("InterviewPreparation"), "JoufswjfxQsfqbsbujpo")

    def test8(self):
        sao = ShiftAlphabetOrder()
        self.assertEqual(sao.solution("YWXyz"), "ZXYza")

    def test9(self):
        sao = ShiftAlphabetOrder()
        self.assertEqual(sao.solution("shift123"), "tijgu123")

    def test10(self):
        sao = ShiftAlphabetOrder()
        self.assertEqual(sao.solution("adZ$56Y"), "beA$56Z")