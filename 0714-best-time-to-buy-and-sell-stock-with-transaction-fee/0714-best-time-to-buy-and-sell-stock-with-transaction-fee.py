class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Given any day I, its max profit status boils down to one of the two status below:
        # (1) buy status:
        #     buy[i] represents the max profit at day i in buy status, given that the last action you
        #     took is a buy action at day K, where K <= i. And you have the right to sell at day i+1,
        #     or do nothing.
        # (2) sell status:
        #     sell[i] represents the max profit at day i in sell status, given that the last action you
        #     took is a sell actionn at day K, where K <= i. And you have the right to buy at day i+1,
        #     or do nothing.
        
        # Base case:
        # We can start from buy status, which means we buy stock at day 0.
        # buy[0] = -prices[0]
        # Or we can start from sell status, which means we sell stock at day 0.
        # Given that we don't have any stock at hand in day 0, we set sell status to be 0.
        # sell[0] = 0
        
        # Status transformation:
        # At day i, we may buy stock(from previous sell status) or do nothing(from previous buy status):
        # buy[i] = max(buy[i-1], sell[i-1]-prices[i])
        # Or
        # At day i, we may sell stock(from previous buy status) or do nothing(from previous sell status):
        # sell[i] = max(sell[i-1], buy[i-1]+prices[i])
        
        # Finally:
        # We will return sell[last_day] as our result, which represents the max profit at the last day,
        # given that you took sell action at any day before the last day.
        
        # We can apply transaction fee at either buy status or sell status.
        
        if len(prices) == 1: return 0
        buy, sell = [0] * len(prices), [0] * len(prices)
        buy[0] = -prices[0]-fee
        for i in range(1, len(prices)):
            buy[i] = max(buy[i-1], sell[i-1]-prices[i]-fee)
            sell[i] = max(sell[i-1], buy[i-1]+prices[i])
        return sell[-1]