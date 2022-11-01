class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        G = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            G[x].append(y)
        for i in range(numCourses):
            if not self.dfs(G, visited, i): return False
        return True
    
    def dfs(self, G, visited, i):
        if visited[i] == -1: return False
        if visited[i] == 1: return True
        visited[i] = -1
        for j in G[i]:
            if not self.dfs(G, visited, j): return False
        visited[i] = 1
        return True