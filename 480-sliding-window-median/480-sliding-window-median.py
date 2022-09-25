from heapq import heappush, heappop
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # To calculate the median, we can maintain divide array into subarray equally: small and large
        # All elements in small are no longer than any element in large.
        # So median would be (largest in small + smallest iin large) / 2 if small's size = large's size.
        # If large's size == small's size + 1, median is the smallest in large.
        
        def move(h1, h2):
            x, i = heapq.heappop(h1)
            heapq.heappush(h2, (-x, i))

        def get_med(h1, h2, k):
            return h2[0][0] * 1. if k & 1 else (h2[0][0]-h1[0][0]) / 2.
        
        small, large = [], []
        for i, x in enumerate(nums[:k]):
            heapq.heappush(small, (-x, i))
        
        for _ in range(k-(k>>1)):
            move(small, large)
        
        ans = [get_med(small, large, k)]
        
        for i, x in enumerate(nums[k:]):
            if x >= large[0][0]:
                heapq.heappush(large, (x, i+k))
                if nums[i] <= large[0][0]:
                    move(large, small)
            else:
                heapq.heappush(small, (-x, i+k))
                if nums[i] >= large[0][0]:
                    move(small, large)
            while small and small[0][1] <= i:
                heapq.heappop(small)
            while large and large[0][1] <= i:
                heapq.heappop(large)
            ans.append(get_med(small, large, k))
        return ans