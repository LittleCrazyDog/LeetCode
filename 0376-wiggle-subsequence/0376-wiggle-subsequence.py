class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        length = 1
        up = None   # current status is increasing or not
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] and up != True:
                length += 1
                up = True
            if nums[i] < nums[i-1] and up != False:
                length += 1
                up = False
        return length