class Solution:
    def findContestMatch(self, n: int) -> str:
        R = tuple(range(1, n+1))
        while len(R) > 2:
            R = tuple((R[i],R[~i]) for i in range(len(R)//2))
        return str(R).replace(' ', '')