class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m, n = len(picture), len(picture[0])
        res = 0
        for j in range(n):
            found = False
            for i in range(m):
                if picture[i][j] == 'B':
                    if found or picture[i].count('B') != 1:
                        found = False
                        break
                    found = True
            if found:
                res += 1
        return res