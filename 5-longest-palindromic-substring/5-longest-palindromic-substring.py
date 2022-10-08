class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            odd = self.helper(s, i, i)
            if len(odd) > len(res): res = odd
            even = self.helper(s, i, i+1)
            if len(even) > len(res): res = even
        return res
    
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]