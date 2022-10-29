class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[-1] - nums[0]
        for i in range(len(nums)-1):
            big = max(nums[-1], nums[i]+2*k)
            small = min(nums[i+1], nums[0]+2*k)
            res = min(res, big-small)
        return res