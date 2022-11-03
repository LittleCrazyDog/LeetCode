class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        G = defaultdict(dict)
        for s, d, w in flights:
            G[s][d] = w
        pq = [(0, src, k+1)]
        vis = [0] * n
        while pq:
            w, x, k = heappop(pq)
            if x == dst: return w
            if vis[x] >= k: continue
            vis[x] = k
            for y, dw in G[x].items():
                heappush(pq, (w+dw, y, k-1))
        return -1