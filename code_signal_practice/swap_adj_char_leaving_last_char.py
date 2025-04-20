'''

You are given a string s.
Your task is to write a function that returns a string in which every pair of adjacent characters in the original string is swapped.
If the string has an odd length, leave the last character as it is.
It is not allowed to use Python built-in functions like reverse() or join() in this task, you should implement the solution without using them.

For example, if you are given the string "abcdef", your function should return "badcfe".
If the string is "hello", your function should return "ehllo".

    # 6 chars -


'''


class Solution:

    def solution(self, inpt_str: str):

        l = len(inpt_str)
        ptr = 0

        if l == 1 or l == 0:
            return inpt_str

        is_str_odd = False
        if l % 2 != 0:
            l = l - 1
            is_str_odd = True

        ret_str = ''
        # abcdef
        while ptr < l:

            ret_str += inpt_str[ptr + 1]
            ret_str += inpt_str[ptr]
            ptr += 2
            if is_str_odd and ptr == l:
                ret_str += inpt_str[ptr]

        return ret_str


if __name__ == '__main__':
    sol = Solution()
    print(sol.solution('H'))
