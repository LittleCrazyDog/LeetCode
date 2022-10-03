class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 < n2:
            return self.findMedianSortedArrays(nums2, nums1) # make sure nums2 is the shorter one.
        
        lo, hi = 0, n2*2
        while lo <= hi:
            mid2 = (lo + hi) // 2
            mid1 = n1 + n2 - mid2
            
            l1 = nums1[(mid1-1)//2] if mid1 != 0 else float('-inf')
            l2 = nums2[(mid2-1)//2] if mid2 != 0 else float('-inf')
            r1 = nums1[(mid1)//2] if mid1 != n1*2 else float('inf')
            r2 = nums2[(mid2)//2] if mid2 != n2*2 else float('inf')
            
            if l1 > r2: lo = mid2 + 1   # nums1's lower half is too big
            elif l2 > r1: hi = mid2 - 1 # nums2's lower half is too big
            else: return (max(l1,l2) + min(r1,r2)) / 2
        
        return -1