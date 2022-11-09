class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        maps = defaultdict(list)
        for i, v in enumerate(colors):
            maps[v].append(i)
        res = []
        for i, c in queries:
            if c in maps:
                index = bisect.bisect_left(maps[c], i)
                if index == 0: res.append(abs(i-maps[c][0]))
                elif index >= len(maps[c]): res.append(i-maps[c][-1])
                else: res.append(min(abs(i-maps[c][index-1]), abs(maps[c][index]-i)))
            else: res.append(-1)                    
        return res