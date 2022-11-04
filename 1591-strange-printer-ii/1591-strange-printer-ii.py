class Box:
    def __init__(self):
        self.top = float('inf')
        self.bot = 0
        self.left = float('inf')
        self.right = 0
    
    def update(self, r, c):
        self.top = min(self.top, r)
        self.bot = max(self.bot, r)
        self.left = min(self.left, c)
        self.right = max(self.right, c)
    
    def colors(self, grid):
        return set(grid[r][c] for r in range(self.top, self.bot+1) for c in range(self.left, self.right+1))

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        R, C = len(targetGrid), len(targetGrid[0])
        boxes = defaultdict(Box)
        for r in range(R):
            for c in range(C):
                boxes[targetGrid[r][c]].update(r, c)
        graph = {color: box.colors(targetGrid) - set([color]) for color, box in boxes.items()}
        seen = set()
        path = set()
        def isCyclic(u):
            if u in seen: return u in path
            seen.add(u)
            path.add(u)
            for v in graph[u]:
                if isCyclic(v): return True
            path.remove(u)
            return False
        for color in boxes.keys():
            if isCyclic(color):
                return False
        return True
        