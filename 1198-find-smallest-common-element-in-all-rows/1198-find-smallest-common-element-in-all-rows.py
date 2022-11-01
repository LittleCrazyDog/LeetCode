class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        c = Counter()
        for row in mat:
            for num in row:
                c[num] += 1
                if c[num] == len(mat):
                    return num
        return -1