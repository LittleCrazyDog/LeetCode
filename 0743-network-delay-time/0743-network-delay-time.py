class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        q, t, G = [(0, k)], {}, defaultdict(list)
        for u, v, w in times:
            G[u].append((v, w))
        while q:
            time, node = heappop(q)
            if node in t: continue
            t[node] = time
            for v, w in G[node]:
                heappush(q, (time+w, v))
        return max(t.values()) if len(t) == n else -1