
'''
Given a string input_string, return a new string in which all occurrences
of character c1 in the original string replaced by c2.

You cannot use any built-in string methods or functions in Python,
such as replace().
'''

class Solution:

    def replace_character(self, input_string, c1, c2):
        # TODO: Replace all occurrences of character `c1` in `input_string` with `c2`

        left = 0
        mid = len(input_string) // 2
        right = len(input_string) - 1
        frst_half_ret_str = ''
        scnd_half_ret_str = ''

        while left < mid or mid <= right:

            if left < mid:
                if input_string[left] == c1:
                    frst_half_ret_str += c2
                else:
                    frst_half_ret_str += input_string[left]

            if mid <= right:
                if input_string[right] == c1:
                    scnd_half_ret_str = c2 + scnd_half_ret_str
                else:
                    scnd_half_ret_str = input_string[right] + scnd_half_ret_str

            left += 1
            right -= 1

        return frst_half_ret_str + scnd_half_ret_str

if __name__ == '__main__':
    sol = Solution()
    print(sol.replace_character("the quick brown fox jumps over the lazy dog", "o", "a"))


