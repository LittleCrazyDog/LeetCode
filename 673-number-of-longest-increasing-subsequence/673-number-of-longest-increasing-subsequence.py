class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # dp stores two things:
        # 1. the Length of longest subsequence ending at this index
        # 2. Number of longest subsequence that end at this index
        dp, longest = [[1, 1] for _ in range(len(nums))], 1
        for i, num in enumerate(nums):
            curr_longest, count = 1, 0
            for j in range(i):
                if nums[j] < num:
                    curr_longest = max(curr_longest, dp[j][0] + 1)
            for j in range(i):
                if dp[j][0] == curr_longest - 1 and nums[j] < num:
                    count += dp[j][1]
            dp[i] = [curr_longest, max(count, 1)]
            longest = max(curr_longest, longest)
        return sum([item[1] for item in dp if item[0] == longest])