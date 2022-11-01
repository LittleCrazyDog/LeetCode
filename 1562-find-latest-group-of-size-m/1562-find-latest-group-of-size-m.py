class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr): return m
        length = [0] * (len(arr) + 2)
        res = -1
        for i, a in enumerate(arr):
            left, right = length[a-1], length[a+1]
            if left == m or right == m:
                res = i
            length[a-left] = length[a+right] = left + right + 1
        return res