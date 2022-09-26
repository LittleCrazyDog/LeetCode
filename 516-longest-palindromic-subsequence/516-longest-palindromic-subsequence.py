class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Top Down DP
        # Let dp(l,r) denote the length of the longest palindromic subsequence of s[l..r].
        # There are 2 options:
        #   - If s[l] == s[r] then dp[l][r] = dp[l+1][r-1] + 2
        #   - Elif s[l] != s[r] then dp[l][r] = max(dp[l+1][r], dp[l][r-1]).
        # Then dp(0, n-1) is our result
        # Complexity:
        # Time: O(N^2), where N <= 1000 is the length of s
        # Space: O(N^2)
        
        n = len(s)
        
        @lru_cache(None)
        def dp(l, r):
            if l > r: return 0  # Return 0 since it's empty string
            if l == r: return 1 # Return 1 since it has 1 character
            if s[l] == s[r]:
                return dp(l+1, r-1) + 2
            return max(dp(l, r-1), dp(l+1, r))
        
        return dp(0, n-1)