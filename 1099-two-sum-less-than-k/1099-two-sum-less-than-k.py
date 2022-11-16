class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        res = -1
        nums.sort()
        for i, val in enumerate(nums):
            target = k - val
            target_index = bisect.bisect_left(nums, target, i+1)
            if target_index != i+1:
                res = max(res, val + nums[target_index - 1])
        return res