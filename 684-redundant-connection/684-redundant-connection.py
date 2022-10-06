class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [-1] * (len(edges) + 1)
        rank = [0] * (len(edges) + 1)
        
        def find(x):
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
                rank[root_y] += 1
                return True
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
                return True
        
        for x, y in edges:
            if not union(x, y):
                return [x, y]