class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        d = defaultdict(list)
        for c, p in zip(pid, ppid): d[p].append(c)
        bfs = [kill]
        for i in bfs: bfs.extend(d.get(i, []))
        return bfs