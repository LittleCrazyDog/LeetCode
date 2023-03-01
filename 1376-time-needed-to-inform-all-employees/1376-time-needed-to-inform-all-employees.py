class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        G = defaultdict(list)
        for i in range(n):
            G[manager[i]].append(i)
        def dfs(u):
            res = 0
            for v in G[u]:
                res = max(res, dfs(v) + informTime[u])
            return res
        return dfs(headID)