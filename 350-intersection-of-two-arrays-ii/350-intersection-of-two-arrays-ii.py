class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Two Pointers Approach
        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1 = pt2 = 0
        res = []
        
        while pt1 < len(nums1) and pt2 < len(nums2):
            if nums1[pt1] > nums2[pt2]:
                pt2 += 1
            elif nums1[pt1] < nums2[pt2]:
                pt1 += 1
            else:
                res.append(nums1[pt1])
                pt1 += 1
                pt2 += 1
        
        return res