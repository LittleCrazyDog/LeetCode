class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Dict Approach (record all nums appeared in one list)
        res = []
        dict = {}
        for i in nums1:
            dict[i] = dict[i] + 1 if i in dict else 1
        for j in nums2:
            if j in dict and dict[j] > 0:
                res.append(j)
                dict[j] = 0
        return res