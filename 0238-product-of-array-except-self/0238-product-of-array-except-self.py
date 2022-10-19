class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        left = right = 1
        for i in range(len(nums)):
            res[i] *= left
            res[-1-i] *= right
            left *= nums[i]
            right *= nums[-1-i]
        return res