class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        index = len(nums) - 1
        curr_sum = 0
        self.memo = {}
        return self.dp(nums, target, index, curr_sum)
    
    def dp(self, nums, target, index, curr_sum):
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]
        
        # Base Cases
        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0
        
        # Decisions
        positive = self.dp(nums, target, index-1, curr_sum + nums[index])
        negative = self.dp(nums, target, index-1, curr_sum - nums[index])
        
        self.memo[(index, curr_sum)] = positive + negative
        return positive + negative