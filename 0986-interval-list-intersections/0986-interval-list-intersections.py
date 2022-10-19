class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = j = 0
        result = []
        while i < len(A) and j < len(B):
            a_start, a_end = A[i]
            b_start, b_end = B[j]
            if a_start <= b_end and b_start <= a_end:
                result.append([max(a_start, b_start), min(a_end, b_end)])
            if a_end <= b_end:
                i += 1
            else:
                j += 1
        return result