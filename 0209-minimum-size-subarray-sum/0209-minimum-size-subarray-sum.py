class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, res = 0, float('inf')
        for j in range(len(nums)):
            target -= nums[j]
            while target <= 0:
                res = min(res, j-i+1)
                target += nums[i]
                i += 1
        return res if res != float('inf') else 0