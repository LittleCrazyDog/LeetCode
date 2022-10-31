class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        startCol, endCol = 0, len(mat[0])-1
        while startCol <= endCol:
            maxRow = 0
            midCol = (startCol+endCol)//2
            for row in range(len(mat)):
                maxRow = row if (mat[row][midCol] >= mat[maxRow][midCol]) else maxRow
            leftIsBig  = midCol-1 >= startCol and mat[maxRow][midCol-1] > mat[maxRow][midCol]
            rightIsBig = midCol+1 <= endCol   and mat[maxRow][midCol+1] > mat[maxRow][midCol]
            if (not leftIsBig) and (not rightIsBig):
                return [maxRow, midCol]
            elif rightIsBig:
                startCol = midCol + 1
            else:
                endCol = midCol - 1
        return []