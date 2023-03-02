class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        imax, imin = 1, 1
        res = nums[0]
        for num in nums:
            if num < 0: imax, imin = imin, imax
            imax = max(num, num*imax)
            imin = min(num, num*imin)
            res = max(res, imax)
        return res