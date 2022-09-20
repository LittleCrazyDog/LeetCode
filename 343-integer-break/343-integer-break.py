class Solution:
    def integerBreak(self, n: int) -> int:
        case = [0,0,1,2,4,6,9]
        if n < 7:
            return case[n]
        dp = case + [0] * (n-6)
        for i in range(7, n+1):
            dp[i] = dp[i-3] * 3
        
        return dp[-1]