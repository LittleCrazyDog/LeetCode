class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))
        while left <= right:
            cur = left**2 + right**2
            if cur == c: return True
            if cur < c:
                left += 1
            else:
                right -= 1
        return False