class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans, M = 0, 10**9+7
        for x in range(n):
            ans = (ans * (1 << (len(bin(x+1))-2))+x+1) % M
        return ans