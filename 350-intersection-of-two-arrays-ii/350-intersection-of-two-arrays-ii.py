class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Dictionary Count Approach
        counts = {}
        res = []
        
        for num in nums1:
            counts[num] = counts.get(num, 0) + 1
            
        for num in nums2:
            if num in counts and counts[num] > 0:
                counts[num] -= 1
                res.append(num)
        
        return res