class Solution:
    def minCut(self, s: str) -> int:
        # Let isPalindrome(l, r) be True if string s[l...r] is palindrome else False
        # Let dp(i) denote the minimum number of palindrome substrings of string s[i...n-1]
        # The answer is dp(0) - 1 which is number minimum cuts need to be made on string s[0...n-1]
        
        n = len(s)
        
        @lru_cache(None)
        def isPalindrome(l, r):
            if l >= r: return True
            if s[l] != s[r]: return False
            return isPalindrome(l+1, r-1)
        
        @lru_cache(None)
        def dp(i):
            if i == n:
                return 0
            res = float('inf')
            for j in range(i, n):
                if isPalindrome(i, j):
                    res = min(res, dp(j+1) + 1)
            return res
        
        return dp(0) - 1