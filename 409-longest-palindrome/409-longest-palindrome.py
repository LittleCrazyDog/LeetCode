class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Clean Code
        # odds = sum(v & 1 for v in Counter(s).values())
        # return len(s) - odds + bool(odds)
        ctr = defaultdict(int)
        for ch in s:
            ctr[ch] += 1
        ret, odd_ctr, sum_odd = 0, 0, 0
        for ch, freq in ctr.items():
            if freq % 2 == 0:
                ret += freq
            else:
                odd_ctr += 1
                sum_odd += freq
        if odd_ctr > 0:
            ret = ret + sum_odd - (odd_ctr - 1)
        return ret