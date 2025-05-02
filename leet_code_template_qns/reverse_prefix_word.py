from collections import deque


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        d = deque()
        idx = 0  # first char index

        for i in range(len(word)):

            if idx == 0:
                if word[i] == ch:
                    idx += 1
                d.appendleft(word[i])
            elif idx > 0:
                d.append(word[i])

        if idx == 0:
            return word
        else:
            return "".join(d)

