class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums_sum = sum(nums)
        nums.sort(reverse=True)
        if nums_sum % k != 0: return False
        target = nums_sum//k
        targets = [target] * k
        
        def dfs(pos):
            if pos == len(nums): return True
            for i in range(k):
                if targets[i] >= nums[pos]:
                    targets[i] -= nums[pos]
                    if dfs(pos+1):
                        return True
                    targets[i] += nums[pos]
                    if targets[i] == target:
                        break
            return False
        
        return dfs(0)