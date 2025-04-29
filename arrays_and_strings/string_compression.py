from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:

        res = []
        if len(chars) == 1:
            return 1

        for c in chars:
            if c in res:
                continue
            else:
                cnt = chars.count(c)
                res.append(c)
                res.append(str(cnt))
                #if not cnt == 1:
                #    res.append(c)
                #    res.append(str(cnt))
                #else:
                #    res.append(c)

        return len(res)

if __name__ == '__main__':
    sol = Solution()
    s = ["a","a","b","b","c","c","c"]
    print(sol.compress(s))




