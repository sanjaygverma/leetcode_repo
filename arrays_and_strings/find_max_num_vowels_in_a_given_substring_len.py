class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        ln = len(s)
        vwls = ['a', 'e', 'i', 'o', 'u']
        if ln == 1 and s in vwls:
            return 1
        elif ln == 0:
            return 0

        l = 0
        r = ln - 1
        max_vowls = 0

        # vowel letters - aeiou

        # generate combinations in a string - this will generate
        # lot of permuation and combinations - so better
        # get the window and check every vowel and update the count in the substring

        # unique version / combinations
        # 5, 4, 3, 2, 1 - uniq
        # 5 * 5 single letters - 25
        # 5 * 2 - ae, io, ua

        # based on the issue need to shift the window to
        # the index where the first vowel starts

        #This logic fails as it is o(kn) for time complexity at 100th test case where k is given
        #TODO need to change to o(n) by traversing

        while l < r:
            s_1 = s[l:l + k]
            cnt = sum(1 for ch in s_1 if ch in vwls)
            max_vowls = max(max_vowls, cnt)
            l += 1
        return max_vowls