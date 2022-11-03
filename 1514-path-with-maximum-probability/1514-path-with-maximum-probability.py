class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        p, G = [0.0] * n, defaultdict(list)
        for index, (a, b) in enumerate(edges):
            G[a].append((b, index))
            G[b].append((a, index))
        p[start] = 1.0
        heap = [(-p[start], start)]
        while heap:
            prob, cur = heappop(heap)
            if cur == end: return -prob
            for neighbor, index in G[cur]:
                if -prob * succProb[index] > p[neighbor]:
                    p[neighbor] = -prob * succProb[index]
                    heappush(heap, (-p[neighbor], neighbor))
        return 0.0