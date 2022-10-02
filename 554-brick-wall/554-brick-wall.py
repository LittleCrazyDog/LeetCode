class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d = defaultdict(int)
        for line in wall:
            i = 0
            for brick in line[:-1]:
                i += brick
                d[i] += 1
        return len(wall) - max(d.values(), default=0)