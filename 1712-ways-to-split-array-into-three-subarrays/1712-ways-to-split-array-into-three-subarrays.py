class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        sz, res, j, k = len(nums), 0, 0, 0
        nums = list(accumulate(nums))
        for i in range(sz - 2):
            while j <= i or (j < sz - 1 and nums[j] < nums[i] * 2):
                j += 1
            while k < j or (k < sz - 1 and nums[k] - nums[i] <= nums[-1] - nums[k]):
                k += 1
            res += k - j
        return res % (10**9+7)