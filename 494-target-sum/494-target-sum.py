class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = Counter({0: 1})
        for x in nums:
            step = Counter()
            for y in count:
                step[y+x] += count[y]
                step[y-x] += count[y]
            count = step
        return count[target]