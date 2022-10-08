class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxs, window = [], deque([])
        for i, x in enumerate(nums):
            while window and window[-1] < x: window.pop()
            window.append(x)
            if i >= k and nums[i-k] == window[0]: window.popleft()
            if i >= k-1: maxs.append(window[0])
        return maxs