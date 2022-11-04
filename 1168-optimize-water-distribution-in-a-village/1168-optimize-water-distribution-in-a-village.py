class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        def find(x):
            if x != uf[x]: uf[x] = find(uf[x])
            return uf[x]
        uf = {i: i for i in range(n+1)}
        w = [[c, 0, i] for i, c in enumerate(wells, 1)]
        p = [[c, i, j] for i, j, c in pipes]
        res = 0
        for c, x, y in sorted(w + p):
            x, y = find(x), find(y)
            if x != y:
                uf[find(x)] = find(y)
                res += c
                n -= 1
            if n == 0:
                return res