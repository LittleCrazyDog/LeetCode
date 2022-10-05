class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans, l, r = [0] * n, 1, k+1
        for i in range(k+1):
            if i % 2:
                ans[i] = r
                r -= 1
            else:
                ans[i] = l
                l += 1
        for i in range(k+1, n):
            ans[i] = i + 1
        
        return ans