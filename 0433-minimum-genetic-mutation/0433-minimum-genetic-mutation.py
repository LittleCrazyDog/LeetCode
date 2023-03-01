class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = deque([(start, 0)])
        bank = set(bank)
        while queue:
            curr, step = queue.popleft()
            if curr == end: return step
            for i in range(len(curr)):
                for c in "AGCT":
                    mutation = curr[:i] + c + curr[i+1:]
                    if mutation in bank:
                        bank.remove(mutation)
                        queue.append((mutation, step+1))
        return -1