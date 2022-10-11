class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.res = 0
        roads = set()
        G = defaultdict(list)
        for u, v in connections:
            roads.add((u, v))
            G[v].append(u)
            G[u].append(v)
        
        def dfs(u, parent):
            self.res += (parent, u) in roads
            for v in G[u]:
                if v == parent: continue
                dfs(v, u)
        
        dfs(0, -1)
        return self.res