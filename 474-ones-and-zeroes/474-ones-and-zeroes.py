class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp(mm, nn, kk), where
        # mm is how many zeros we still allowed to take
        # nn is how many ones we still allowed to take
        # kk is how many pairs out of k we already used
        
        # 1. if mm < 0 or nn < 0, we return float('-inf'), because we take more zeros or ones than allowed
        # 2. if kk == len(strs), it means, that we out of pairs, return 0
        # 3. finally, we can have two options: either take the last pair or not, and we choose the maximum
        
        # Time and Space Complexity is O(mnk), where k is the number of strings, because we have this number
        # of states and only 2 transitions from given state
        
        xy = [[s.count('0'), s.count('1')] for s in strs]
        
        @lru_cache(None)
        
        def dp(mm, nn, kk):
            if mm < 0 or nn < 0: return float('-inf')
            if kk == 0: return 0
            x, y = xy[kk-1]
            return max(1 + dp(mm-x, nn-y, kk-1), dp(mm, nn, kk-1))
        
        return dp(m, n, len(strs))