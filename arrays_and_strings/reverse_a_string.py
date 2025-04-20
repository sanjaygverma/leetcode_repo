from typing import List




class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # "hello"

        i = 0
        half = len(s) // 2
        j = len(s) - 1

        print(s)

        while i < half and half <= j:
            bkpos_char = s[j]
            fwdpos_char = s[i]
            s[i] = bkpos_char
            s[j] = fwdpos_char
            i += 1
            j -= 1

        print(s)


#Solution.reverseString(ls)

if __name__ == '__main__':
    #ls = ["h", "e", "l", "l", "o"]
    ls = ["r", "a", "c", "e", "c", "a", "r"]
    s = Solution()
    s.reverseString(ls)
    #Solution.reverseString(self, s=ls)
