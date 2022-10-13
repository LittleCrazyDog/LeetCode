class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited, q, depth = set(deadends), deque(['0000']), -1
        
        while q:
            depth += 1
            for _ in range(len(q)):
                code = q.popleft()
                if code == target: return depth
                if code in visited: continue
                visited.add(code)
                q.extend(self.successors(code))
        return -1
    
    def successors(self, code):
        res = []
        for i, ch in enumerate(code):
            num = int(ch)
            res.append(code[:i] + str((num - 1) % 10) + code[i+1:])
            res.append(code[:i] + str((num + 1) % 10) + code[i+1:])
        return res