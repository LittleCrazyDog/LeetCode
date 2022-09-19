class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # boundary case
        if len(prices) == 1: return 0
        
        s0 = [0 for _ in range(len(prices))]
        s1 = [0 for _ in range(len(prices))]
        s2 = [0 for _ in range(len(prices))]
        
        # s0[i] = max(s0[i-1], s2[i-1])
        # s1[i] = max(s1[i-1], s0[i-1]-prices[i])
        # s2[i] = s1[i-1] + prices[i]
        
        # base case
        s0[0] = 0   # At the beginning, you don't have any stock if you just rest
        s1[0] = -prices[0]  # After buy, you should have -prices[0] profit. Be positive!
        s2[0] = float('-inf')   # Lower base case
        
        for i in range(1, len(prices)):
            s0[i] = max(s0[i-1], s2[i-1])
            s1[i] = max(s1[i-1], s0[i-1]-prices[i])
            s2[i] = s1[i-1] + prices[i]
        
        return max(s0[-1], s2[-1])