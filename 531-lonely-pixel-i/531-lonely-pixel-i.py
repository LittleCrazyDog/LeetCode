class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        return sum(col.count('B') == 1 == picture[col.index('B')].count('B') for col in zip(*picture))