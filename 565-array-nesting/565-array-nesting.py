class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        seen, res = [0] * len(nums), 0
        for num in nums:
            cnt = 0
            while not seen[num]:
                seen[num], cnt, num = 1, cnt+1, nums[num]
            res = max(res, cnt)
        return res