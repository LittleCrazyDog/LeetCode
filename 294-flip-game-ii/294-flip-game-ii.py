class Solution:
    def canWin(self, s: str) -> bool:
        memo = {}
        def can(s):
            if s not in memo:
                memo[s] = any(s[i:i+2] == '++' and not can(s[:i] + '-' + s[i+2:]) for i in range(len(s)))
            return memo[s]
        return can(s)