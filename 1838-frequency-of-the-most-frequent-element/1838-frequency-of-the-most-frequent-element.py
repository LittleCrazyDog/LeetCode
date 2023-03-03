class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        i = 0
        nums.sort()
        for j in range(len(nums)):
            k += nums[j]
            if k < nums[j] * (j - i + 1):
                k -= nums[i]
                i += 1
        return j - i + 1
        
        
        # i = 0
        # nums.sort()
        # for j in range(len(nums)):
        #     k += nums[j]
        #     if k < nums[j] * (j - i + 1):
        #         k -= nums[i]
        #         i += 1
        # return j - i + 1