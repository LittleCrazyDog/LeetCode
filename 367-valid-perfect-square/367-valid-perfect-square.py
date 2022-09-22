class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Math Trick for Square Number is 1 + 3 + 5 + ... + (2n-1)
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0