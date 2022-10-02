class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # L, R orders must be the same
        if start.replace('X', '') != end.replace('X', ''):
            return False
        
        n = len(start)
        startL = [i for i in range(n) if start[i] == 'L']
        endL = [i for i in range(n) if end[i] == 'L']
        startR = [i for i in range(n) if start[i] == 'R']
        endR = [i for i in range(n) if end[i] == 'R']
        
        for i, j in zip(startL, endL):
            if i < j:
                return False
        
        for i, j in zip(startR, endR):
            if i > j:
                return False
        
        return True