class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # BFS Approach
        g = {x:[] for x in range(n)}
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        ret = 0
        for i in range(n):
            queue = [i]
            ret += 1 if i in g else 0
            for j in queue:
                if j in g:
                    queue += g[j]
                    del g[j]
        
        return ret