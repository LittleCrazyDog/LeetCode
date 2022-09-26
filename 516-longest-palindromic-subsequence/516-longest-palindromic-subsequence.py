class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Bottom Up DP (Space Optimized)
        # Since we need to access up to 2 dp states: current dp and previous dp state dpPrev
        # So we can optimize to achieve O(N) in Space Complexity
        # Complexity:
        # Time: O(N^2), where N <= 1000 is the length of s
        # Space: O(N)
        
        n = len(s)
        dp, dpPrev = [0] * n, [0] * n
        
        for i in range(n-1, -1, -1):
            dp[i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[j] = dpPrev[j-1] + 2
                else:
                    dp[j] = max(dpPrev[j], dp[j-1])
            dp, dpPrev = dpPrev, dp
        
        return dpPrev[n-1]