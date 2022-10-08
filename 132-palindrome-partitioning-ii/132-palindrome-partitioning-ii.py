class Solution:
    def minCut(self, s: str) -> int:
#         # Let isPalindrome(l, r) be True if string s[l...r] is palindrome else False
#         # Let dp(i) denote the minimum number of palindrome substrings of string s[i...n-1]
#         # The answer is dp(0) - 1 which is number minimum cuts need to be made on string s[0...n-1]
        
#         n = len(s)
        
#         @lru_cache(None)
#         def isPalindrome(l, r):
#             if l >= r: return True
#             if s[l] != s[r]: return False
#             return isPalindrome(l+1, r-1)
        
#         @lru_cache(None)
#         def dp(i):
#             if i == n:
#                 return 0
#             res = float('inf')
#             for j in range(i, n):
#                 if isPalindrome(i, j):
#                     res = min(res, dp(j+1) + 1)
#             return res
        
#         return dp(0) - 1
        if s == s[::-1]: return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        # algorithm
        cut = [x for x in range(-1,len(s))]  # cut numbers in worst case (no palindrome)
        for i in range(len(s)):
            r1, r2 = 0, 0
            # use i as origin, and gradually enlarge radius if a palindrome exists
            # odd palindrome
            while i-r1 >= 0 and i+r1 < len(s) and s[i-r1] == s[i+r1]:
                cut[i+r1+1] = min(cut[i+r1+1], cut[i-r1]+1)
                r1 += 1
            # even palindrome
            while i-r2 >= 0 and i+r2+1 < len(s) and s[i-r2] == s[i+r2+1]:
                cut[i+r2+2] = min(cut[i+r2+2], cut[i-r2]+1)
                r2 += 1
        return cut[-1]