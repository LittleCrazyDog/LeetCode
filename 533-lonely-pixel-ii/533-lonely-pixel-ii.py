class Solution:
    def findBlackPixel(self, picture: List[List[str]], target: int) -> int:
        row = [r.count('B') for r in picture]
        col = [c.count('B') for c in zip(*picture)]
        
        loneP = 0
        
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] != 'B':
                    continue
                if row[i] == target and col[j] == target:
                    if all(picture[k] == picture[i] for k in range(len(picture)) \
                          if picture[k][j] == 'B'):
                        loneP += 1
        return loneP