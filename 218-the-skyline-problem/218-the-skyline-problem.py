class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Scan all (x, height) points from left to right, if max height changes, record it in final result
        # To know the max height at any x position, we need a max_heap to record (height, x)
        
        # for the same x, (x, -H) should be in front of (x, 0)
        x_height_right_tuples = sorted([(L,-H,R) for L,R,H in buildings] + [(R, 0, "doesn't matter") for _,R,_ in buildings])
        # (0, float('inf')) is always in max_heap, so max_heap[0] is always valid
        result, max_heap = [[0, 0]], [(0, float('inf'))]
        for x, negative_height, R in x_height_right_tuples:
            while x >= max_heap[0][1]:
                # reduce max height up to date, i.e. only consider max height in the right side of line x
                heapq.heappop(max_heap)
            if negative_height:
                # Consider each height, as it may be the potential max height
                heapq.heappush(max_heap, (negative_height, R))
            curr_max_height = -max_heap[0][0]
            if result[-1][1] != curr_max_height:
                result.append([x, curr_max_height])
        return result[1:]