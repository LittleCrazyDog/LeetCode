class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def find(u):
            if p[u] != u:
                p[u] = find(p[u])
            return p[u]
        
        def deleteCycle(edge):
            u, v = edge
            while u != v and u in parents:
                u = parents[u]
            return u == v
        
        candidates = []
        parents = {}
        for u, v in edges:
            if v not in parents:
                parents[v] = u
            else:
                candidates.append((parents[v], v))
                candidates.append((u, v))
        
        if candidates:
            return candidates[0] if deleteCycle(candidates[0]) else candidates[1]
        else:
            p = list(range(len(edges)+1))
            for edge in edges:
                u, v = map(find, edge)
                if u == v:
                    return edge
                p[u] = p[v]