class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for c in s:
            i = ord(c) - ord('a')
            dp[i] = max(dp[max(0,i-k):min(25,i+k)+1]) + 1
        return max(dp)