class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]
        
        def union(x, y):
            x, y = find(x), find(y)
            if x == y: return 0
            root[x] = y
            return 1
        
        res = e1 = e2 = 0
        
        root = list(range(n+1))
        for t, i, j in edges:
            if t == 3:
                if union(i, j):
                    e1 += 1
                    e2 += 1
                else:
                    res += 1
        temproot = root[:]

        for t, i, j in edges:
            if t == 1:
                if union(i, j):
                    e1 += 1
                else:
                    res += 1
        
        root = temproot[:]
        
        for t, i, j in edges:
            if t == 2:
                if union(i, j):
                    e2 += 1
                else:
                    res += 1
        
        return res if e1 == e2 == n-1 else -1