class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        G = [[[], []] for _ in range(n)]
        for i, j in redEdges: G[i][0].append(j)
        for i, j in blueEdges: G[i][1].append(j)
        res = [[0, 0]] + [[n*2, n*2] for _ in range(n-1)]
        bfs = [[0, 0], [0, 1]]
        for i, c in bfs:
            for j in G[i][c]:
                if res[j][c] == n*2:
                    res[j][c] = res[i][1-c] + 1
                    bfs.append([j, 1-c])
        return [x if x < n*2 else -1 for x in map(min, res)]