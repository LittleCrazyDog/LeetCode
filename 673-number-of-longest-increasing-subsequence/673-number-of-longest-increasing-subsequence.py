class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # dp stores two things:
        # 1. the Length of longest subsequence ending at this index
        # 2. Number of longest subsequence that end at this index
        dp = [[1, 1] for _ in range(len(nums))]
        max_for_all = 1
        for i, num in enumerate(nums):
            max_len, count = 1, 0
            for j in range(i):
                if nums[j] < num:
                    if dp[j][0] + 1 > max_len:
                        max_len = dp[j][0] + 1
                        count = 0
                    if dp[j][0] + 1 == max_len:
                        count += dp[j][1]
            dp[i] = [max_len, max(count, dp[i][1])]
            max_for_all = max(max_for_all, max_len)
        return sum([item[1] for item in dp if item[0] == max_for_all])