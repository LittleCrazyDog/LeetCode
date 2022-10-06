class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        times = ceil(len(b)/len(a))
        for i in range(2):
            if b in (a * (times + i)):
                return times + i
        return -1