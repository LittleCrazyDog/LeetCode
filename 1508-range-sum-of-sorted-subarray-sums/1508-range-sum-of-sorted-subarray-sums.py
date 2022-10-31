class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        h = [(x, i) for i, x in enumerate(nums)]
        heapify(h)
        res = 0
        for k in range(1, right+1):
            x, i = heappop(h)
            if k >= left: res += x
            if i+1 < len(nums): heappush(h, (x+nums[i+1], i+1))
        return res % (10**9+7)