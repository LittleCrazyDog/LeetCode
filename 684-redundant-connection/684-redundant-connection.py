class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        p = [x for x in range(len(edges) + 1)]
        
        def find(x):
            if p[x] != x: p[x] = find(p[x])
            return p[x]
        
        def union(x, y):
            if find(x) == find(y): return True
            p[find(x)] = find(y)
        
        for x, y in edges:
            if union(x, y): return [x, y]