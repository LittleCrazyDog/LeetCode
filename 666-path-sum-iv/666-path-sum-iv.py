class Solution:
    def pathSum(self, nums: List[int]) -> int:
        # l means for node(i, j), it occurs l[i, j] times in all paths
        # s means using node(i, j) as root, it's path sum is s[i, j]
        l = {}
        s = {}
        for i in nums[::-1]:
            a, b, c = i // 100, i // 10 % 10, i % 10
            l[a, b] = max(1, l.get((a+1, b*2-1), 0) + l.get((a+1, b*2), 0))
            s[a, b] = s.get((a+1, b*2-1), 0) + s.get((a+1, b*2), 0) + l[a, b] * c
        return s.get((1,1), 0)