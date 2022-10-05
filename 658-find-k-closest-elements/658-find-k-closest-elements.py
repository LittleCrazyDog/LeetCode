class Solution:
    def findClosestElements(self, A: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(A) - k
        while left < right:
            mid = (left + right) // 2
            if x - A[mid] > A[mid+k] - x:
                left = mid + 1
            else:
                right = mid
        return A[left:left+k]