class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # BFS (same as word ladder)
        queue = deque([(start, 0)])
        bankSet = set(bank)
        
        while queue:
            curr, step = queue.popleft()
            if curr == end:
                return step
            for i in range(len(curr)):
                for c in "AGCT":
                    mutation = curr[:i] + c + curr[i+1:]
                    if mutation in bankSet:
                        bankSet.remove(mutation)
                        queue.append((mutation, step+1))
        
        return -1