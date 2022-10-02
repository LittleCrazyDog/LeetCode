class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows = len(isConnected)
        seen = set()
        count = 0
        
        def bfs(row_index):
            q = deque([row_index])
            
            while q:
                idx = q.popleft()
                for friend, is_friend in enumerate(isConnected[idx]):
                    if is_friend == 1 and friend not in seen:
                        seen.add(friend)
                        q.append(friend)
        
        for r in range(rows):
            if r not in seen:
                seen.add(r)
                bfs(r)
                count += 1
        
        return count