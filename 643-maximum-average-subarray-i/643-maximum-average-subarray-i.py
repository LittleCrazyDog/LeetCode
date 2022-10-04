class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        P = [0]
        for x in nums:
            P.append(P[-1] + x)
        
        ma = max(P[i+k] - P[i] for i in range(len(nums)-k+1))
        
        return ma / float(k)