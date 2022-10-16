class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for n in range(num+1):
            if n + int(str(n)[::-1]) == num:
                return True
        return False