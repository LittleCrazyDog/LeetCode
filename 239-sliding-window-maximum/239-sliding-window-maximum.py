class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += [i]
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += [nums[d[0]]]
        return out