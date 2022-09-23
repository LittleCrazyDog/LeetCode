class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # Bottom Up DP
        # Let dp[i] denote the number of arithmetic subarray ends at nums[i]
        n = len(nums)
        dp = [0] * n
        ans = 0
        for i in range(2, n):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                dp[i] = dp[i-1] + 1
            ans += dp[i]
        return ans