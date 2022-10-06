class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s = list(map(len, s.replace('10', '1 0').replace('01', '0 1').split()))
        return sum(min(a, b) for a, b in zip(s, s[1:]))