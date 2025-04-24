class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        ln = len(s)
        vwls = ['a', 'e', 'i', 'o', 'u']

        if ln == 1 and s in vwls:
            return 1
        elif ln == 0:
            return 0

        m_vwl_cnt = 0
        c_vwl_cnt = 0

        for idx in range(k):
            if s[idx] in vwls:
                c_vwl_cnt += 1

        m_vwl_cnt = max(c_vwl_cnt, m_vwl_cnt)

        for idx in range(k, ln, 1):

            if s[idx-k] in vwls:
                c_vwl_cnt -= 1

            if s[idx] in vwls:
                c_vwl_cnt += 1

            m_vwl_cnt = max(m_vwl_cnt, c_vwl_cnt)

            if m_vwl_cnt == k:
                break

        return m_vwl_cnt

