class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        G = defaultdict(set)
        indegree = [0] * (n+1)
        for s, e in relations:
            G[s].add(e)
            indegree[e] += 1
        queue = deque([i for i in range(1, n+1) if indegree[i] == 0])
        level = 0
        while queue:
            level += 1
            size = len(queue)
            for _ in range(size):
                v = queue.popleft()
                for adj in G[v]:
                    indegree[adj] -= 1
                    if indegree[adj] == 0:
                        queue.append(adj)
        return level if sum(indegree) == 0 else -1
        
        