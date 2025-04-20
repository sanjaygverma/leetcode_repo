#Given a string, you need to return a new string where every letter is shifted to its right by
# one place in alphabetical order. The last letters z and Z should be
# replaced with the first ones: a and A, respectively.
# If the character isn't a letter, it should stay the same.
#It is not allowed to use string built-in methods here.
#For example, given the string "abc123XYz!", the function should return "bcd123YZa!".


class ShiftAlphabetOrder:

    def solution(self, s: str) -> str:

        up_cse = {chr(i) : '' for i in range(65, 91)}
        low_cse = {chr(i) : '' for i in range (97, 123)}
        d = up_cse | low_cse
        shftd_str = ''

        for a in s:
            if a in d:
                ascii_val = ord(a)

                if ascii_val == 122:
                    shftd_str += chr(97)
                elif ascii_val == 90:
                    shftd_str += chr(65)
                else:
                    shftd_str += chr(ascii_val+1)
            else:
                shftd_str += a
        return shftd_str


if __name__ == '__main__':
    salo = ShiftAlphabetOrder('abc123XYz!')

