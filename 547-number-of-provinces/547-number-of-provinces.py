class UF:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.count = 0
    
    def size(self):
        return self.count
    
    def add(self, x):
        if x in self.parent:
            return
        self.parent[x] = x
        self.rank[x] = 1
        self.count += 1
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        ru, rv = self.find(u), self.find(v)
        if ru == rv:
            return
        if self.rank[ru] < self.rank[rv]:
            self.parent[ru] = rv
        elif self.rank[ru] > self.rank[rv]:
            self.parent[rv] = ru
        else:
            self.parent[rv] = ru
            self.rank[ru] += 1
        
        self.count -= 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UF()
        m, n = len(isConnected), len(isConnected[0])
        for i in range(m):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.add(i)
                    uf.add(j)
                    uf.union(i, j)
        return uf.size()