class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Binary Search Method
        left, right = 0, num
        
        while left <= right:
            mid = left + (right-left) // 2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                right = mid - 1
            else:
                left = mid + 1
        
        return False