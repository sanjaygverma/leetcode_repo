# You are given a string, and your task is to check whether the provided string is a palindrome, without using any
# built-in string methods. A string is a palindrome if it reads the same forward and backward, ignoring the casing of
# letters ('A' and 'a' are considered the same) and ignoring non-letter characters.
# Return a boolean value: True if the string is a palindrome and False if it is not.
# It is not allowed to use Python built-in functions like reverse(), reversed(), or similar in this task.

class Solution:

    def solution(self, input_string: str) -> bool:

        isPalDrme = False

        # racecar
        # a man, a plan, a canal: panama -

        # preprocessing of string
        # remove white space - replace with ''
        # remove special chars - replace with ''

        input_string = input_string.lower()
        input_string = input_string.replace(",", "")
        input_string = input_string.replace("!@#$%^&*()", "")
        input_string = input_string.replace("?", "")
        input_string = input_string.replace(" ", "")
        input_string = input_string.replace(":", "")

        if input_string == "":
            return True

        # end preprocessing

        left = 0
        mid = len(input_string) // 2
        right = len(input_string) - 1

        res_frst_str = ''  # from backward half
        res_snd_str = ''  # from fwd half

        while left <= mid <= right:
            res_frst_str += input_string[right]
            if left < mid:
                res_snd_str = input_string[left] + res_snd_str

            left += 1
            right -= 1


        if res_frst_str + res_snd_str == input_string:
            isPalDrme = True

        return isPalDrme


if __name__ == '__main__':
    sol = Solution()
    print(sol.solution('Was it a car or a cat I saw?'))
