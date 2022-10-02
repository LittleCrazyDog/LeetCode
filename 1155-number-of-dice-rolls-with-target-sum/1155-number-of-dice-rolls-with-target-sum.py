class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # Let dp(d, f, target) be the number of possible dice rolls for the given parameters
        
        # dp(d, f, target) = dp(d-1, f, target-1) + dp(d-1, f, target-2) + ... + dp(d-1, f, target-f)
        # The base case occur when d = 0. We can make target = 0 with 0 dice, but nothing else
        # So dp(0, f, t) = 0 if t != 0, and dp(0, f, 0) = 1
        
        # Use memoization to avoid repeated calculations and don't consider negative targets
        
        memo = {}
        
        def dp(d, target):
            if d == 0:
                return 0 if target > 0 else 1
            if (d, target) in memo:
                return memo[(d, target)]
            to_return = 0
            for k in range(max(0, target-f), target):
                to_return += dp(d-1, k)
            memo[(d, target)] = to_return
            return to_return
        return dp(d, target) % (10**9 + 7)