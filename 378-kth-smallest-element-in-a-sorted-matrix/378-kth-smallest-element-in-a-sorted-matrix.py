class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])  # For general, the matrix need not be a square
        
        def countLessOrEqual(x):
            cnt = 0
            c = n - 1   # start with the rightmost column
            for r in range(m):
                while c >= 0 and matrix[r][c] > x: c -= 1    # decrease column until matrix[r][c] <= x
                cnt += (c+1)
            return cnt
        
        left, right = matrix[0][0], matrix[-1][-1]
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if countLessOrEqual(mid) >= k:
                ans = mid
                right = mid - 1 # try to looking for a smaller value in the left side
            else:
                left = mid + 1  # try to looking for a bigger value in the right side
        
        return ans
        