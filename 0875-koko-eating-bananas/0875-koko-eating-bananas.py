class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.ok(piles, h, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
    
    def ok(self, piles, h, k):
        return sum([ceil(pile/k) for pile in piles]) <= h
        
        
        
        
#         lo, hi = 1, max(piles)
        
#         while lo < hi:
#             k = (lo + hi) // 2
#             if self.ok(k, piles, h):
#                 hi = k
#             else:
#                 lo = k+1
#         return lo
    
#     def ok(self, k, piles, h):
#         hoursNeed = [ceil(pile/k) for pile in piles]
#         return sum(hoursNeed) <= h