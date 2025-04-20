from typing import List


class FindVowelPosns:

    def solution(self, s: str) -> List[str]:

        left = 0
        last_indx = len(s)
        mid = len(s) // 2


        if last_indx % 2 != 0:
            mid += 1

        right = mid

        vowls = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        lst_till_mid = list()
        lst_midtoend = list()

        while left < mid or right < last_indx:

            if left < mid:
                if s[left] in vowls:
                    lst_till_mid.append(left)

            if right < last_indx:
                if s[right] in vowls:
                    lst_midtoend.append(right)

            left += 1
            right += 1

        rtls = [*lst_till_mid, *lst_midtoend]
        return rtls


if __name__ == '__main__':
    fvp = FindVowelPosns()
    print(fvp.solution('hello'))
