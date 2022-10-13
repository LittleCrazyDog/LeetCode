class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # Let dp[i][d] denotes the number of subsequences (have at least 2 numbers) that ends with nums[i]
        # and its common difference is d.
        # For i in [1..n-1]
        #   For j in [0..i-1]
        #       diff = nums[i] - nums[j]
        #       dp[i][diff] += dp[j][diff] + 1
        #       res += dp[j][diff]
        
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        
        res = 0
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                cnt = 0
                if diff in dp[j]:
                    cnt = dp[j][diff]
                dp[i][diff] += cnt+1
                res += cnt
        return res