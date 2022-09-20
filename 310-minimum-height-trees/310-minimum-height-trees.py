class Solution:
    def findMinHeightTrees(self, n: int, E: List[List[int]]) -> List[int]:
        # 2*DFS Approach
        G, seen = defaultdict(set), [False] * n
        for u, v in E:
            G[u].add(v)
            G[v].add(u)
        
        def dfs(i):
            if seen[i]: return []
            longest_path = []
            seen[i] = True
            for adj in G[i]:
                if not seen[adj]:
                    path = dfs(adj)
                    if len(path) > len(longest_path):
                        longest_path = path
            longest_path += [i]
            seen[i] = False
            return longest_path
        
        path = dfs(dfs(0)[0])
        return set([path[len(path)//2], path[(len(path)-1)//2]])