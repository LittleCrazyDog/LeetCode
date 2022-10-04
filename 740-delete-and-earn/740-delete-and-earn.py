class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = [0] * 10001
        for num in nums:
            points[num] += num
        return self.rob(points)
    
    def rob(self, nums):
        last, curr = 0, 0
        for num in nums:
            last, curr = curr, max(last+num, curr)
        return curr