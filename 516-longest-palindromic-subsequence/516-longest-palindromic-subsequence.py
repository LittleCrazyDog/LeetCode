class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Bottom Up DP
        # Let dp[l][r] denote the length of the longest palindromic subsequence of s[l..r].
        # There are 2 options:
        #   - If s[l] == s[r] then dp[l][r] = dp[l+1][r-1] + 2
        #   - Elif s[l] != s[r] then dp[l][r] = max(dp[l+1][r], dp[l][r-1]).
        # Then dp[0][n-1] is our result
        # Complexity:
        # Time: O(N^2), where N <= 1000 is the length of s
        # Space: O(N^2)
        
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1]