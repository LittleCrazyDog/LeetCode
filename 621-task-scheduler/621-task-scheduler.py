class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 6's A(max), cooldown = 2
        # (max-1) * (1+cooldown) + 1
        # A cl cl A cl cl A cl cl A cl cl A cl cl A
        # 5 * 3 + 1 = 16
        if n == 0: return len(tasks)
        tasks_count = list(Counter(tasks).values())
        M = max(tasks_count)
        M_count = tasks_count.count(M)
        return max(len(tasks), (M-1)*(1+n)+M_count)