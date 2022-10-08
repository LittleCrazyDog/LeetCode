class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        cps = set()
        lb = defaultdict(list)
        for l, r, h in buildings:
            cps.add(l)
            cps.add(r)
            lb[l].append((-h, r))
        cps = sorted(cps)
        heap = []
        res = []
        for cp in cps:
            for ele in lb.get(cp, []):
                heapq.heappush(heap, ele)
            while heap and heap[0][1] <= cp:
                heapq.heappop(heap)
            critical_height = -heap[0][0] if heap else 0
            if not res or res[-1][1] != critical_height:
                res.append([cp, critical_height])
        return res