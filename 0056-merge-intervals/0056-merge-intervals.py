class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] > output[-1][1]:
                output.append(intervals[i])
            else:
                output[-1][1] = max(output[-1][1], intervals[i][1])
        return output