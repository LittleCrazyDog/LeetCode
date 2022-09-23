class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # @cache
        # def subsetSum(s, i):
        #     if s == 0: return True
        #     if i >= len(nums) or s < 0: return False
        #     return subsetSum(s-nums[i], i+1) or subsetSum(s, i+1)
        # total_sum = sum(nums)
        # return total_sum & 1 == 0 and subsetSum(total_sum // 2, 0)
        
        # total_sum = sum(nums)
        # if total_sum & 1: return False
        # half_sum = total_sum // 2
        # dp = [True] + [False] * half_sum
        # for num in nums:
        #     for j in range(half_sum, num-1, -1):
        #         dp[j] |= dp[j-num]
        # return dp[half_sum]
        
        total_sum = sum(nums)
        if total_sum & 1: return False
        half_sum, dp = total_sum // 2, 1
        for num in nums:
            dp |= dp << num
        return dp & 1 << half_sum