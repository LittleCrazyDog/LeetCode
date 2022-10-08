class Solution:
    def candy(self, ratings: List[int]) -> int:
        n, res = len(ratings), [1] * len(ratings)
        
        for i in range(n-1):
            if ratings[i] < ratings[i+1]:
                res[i+1] = max(res[i+1], res[i]+1)
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i], res[i+1]+1)
        
        return sum(res)