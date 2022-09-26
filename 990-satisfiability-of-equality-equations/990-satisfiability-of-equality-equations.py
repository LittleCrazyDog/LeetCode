class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        # 1. make prep
        graph = collections.defaultdict(set)
        check = set()
        
        # 2. construct graph
        for eq in equations:
            if eq[1:3] == "!=":
                a, b = eq.split("!=")
                check.add((a, b))
            else:
                a, b = eq.split("==")
                graph[a].add(b)
                graph[b].add(a)
                
        # 3. DFS/BFS helper fn
        def bfs(u, target):
            q = collections.deque([u])
            visited = set()
            while q:
                u = q.popleft()
                if u == target:
                    return True
                if u not in visited:
                    visited.add(u)
                    for v in graph[u]:
                        if v not in visited:
                            q.append(v)
            return False
        
        # 4. actual work
        for a, b in check:
            if bfs(a, b):
                return False
        return True