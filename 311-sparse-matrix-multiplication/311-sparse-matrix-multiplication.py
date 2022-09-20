class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, n, l = len(A), len(A[0]), len(B[0])
        C = [[0 for _ in range(l)] for _ in range(m)]
        tableB = {}
        for k, row in enumerate(B):
            tableB[k] = {}
            for j, eleB in enumerate(row):
                if eleB: tableB[k][j] = eleB
        for i, row in enumerate(A):
            for k, eleA in enumerate(row):
                if eleA:
                    for j, eleB in tableB[k].items():
                        C[i][j] += eleA * eleB
        return C