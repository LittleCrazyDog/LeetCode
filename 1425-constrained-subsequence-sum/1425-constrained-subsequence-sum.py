class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        window = deque([])
        for i in range(len(nums)):
            nums[i] += window[0] if window else 0
            while window and window[-1] < nums[i]: window.pop()
            if nums[i] > 0: window.append(nums[i])
            if i >= k and window and window[0] == nums[i-k]: window.popleft()
        return max(nums)