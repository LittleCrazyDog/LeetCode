class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if d[x] != x: d[x] = find(d[x])
            return d[x]
        def union(x, y):
            d[find(x)] = find(y)
        d = list(range(n))
        for x, y in edges:
            union(x, y)
        return len(set([find(x) for x in d]))