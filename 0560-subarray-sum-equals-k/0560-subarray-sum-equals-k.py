class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = sums = 0
        d = defaultdict(int)
        d[0] = 1
        for i in range(len(nums)):
            sums += nums[i]
            count += d[sums-k]
            d[sums] += 1
        return count