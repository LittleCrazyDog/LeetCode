class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        dist[0][0] = 0
        minHeap = [(0, 0, 0)]
        while minHeap:
            d, r, c = heappop(minHeap)
            if d > dist[r][c]: continue
            if r == m - 1 and c == n - 1: return d
            for i, j in (0, -1), (0, 1), (-1, 0), (1, 0):
                nr, nc = r + i, c + j
                if 0 <= nr < m and 0 <= nc < n:
                    newDist = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if dist[nr][nc] > newDist:
                        dist[nr][nc] = newDist
                        heappush(minHeap, (dist[nr][nc], nr, nc))