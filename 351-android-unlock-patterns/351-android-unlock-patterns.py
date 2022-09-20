class Solution:
    def __init__(self):
        self.has_obstacle = {(1,3):2, (1,7):4, (1,9):5, (2,8):5, (3,1):2, (3,7):5, (3,9):6, (4,6):5, (6,4):5, (7,1):4, (7,3):5, (7,9):8, (8,2):5, (9,1):5, (9,3):6, (9,7):8}
    
    def numberOfPatterns(self, m: int, n: int) -> int:
        self.validPatterns = 0
        for num in range(1, 10):
            self.visited = set()
            self._getValidWays(num, 1, m, n)
        return self.validPatterns
    
    def _getValidWays(self, num, count, m, n):
        # consider the valid patterns only in length(m to n)
        if m <= count <= n:
            self.validPatterns += 1
        # after reaching path count 'n', we need not go on any further
        if count == n:
            return
        
        self.visited.add(num)
        for nextNum in range(1, 10):
            if nextNum not in self.visited:
                # if a nextNum has an obstacle while starting from num, and is not visited previously, don't consider this path.
                if (num, nextNum) in self.has_obstacle and self.has_obstacle[(num, nextNum)] not in self.visited:
                    continue
                self._getValidWays(nextNum, count+1, m, n)
        
        self.visited.remove(num)