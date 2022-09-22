class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        r = curr = sum(i * j  for i, j in enumerate(nums))
        s = sum(nums)
        k = len(nums)
        
        while nums:
            curr += s - nums.pop() * k
            r = max(curr, r)
        
        return r