class Solution:
    def lastRemaining(self, n: int) -> int:
        def helper(n, isLeft):
            if n == 1: return 1
            if isLeft:
                return 2 * helper(n // 2, 0)
                # if started from left side the odd elements will be removed, the only remaining ones will be the even
                # [1 2 3 4 5 6 7 8] => [2 4 6 8] which equals 2 * [1 2 3 4]
            elif (n % 2 == 1):
                return 2 * helper(n // 2, 1)
                # same as left side the odd elements will be removed
            else:
                return 2 * helper(n // 2, 1) - 1
                # even elements will be removed and the only left ones will be
                # [1 2 3 4 5 6] => [1 3 5] which equals 2 * [1 2 3] - 1
        
        return helper(n, 1)