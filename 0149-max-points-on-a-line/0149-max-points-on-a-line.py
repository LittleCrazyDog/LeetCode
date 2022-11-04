class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # edge case: return 0 for 0 point, 1 for 1 point
        if len(points) < 2: return len(points)
        
        def gcd(a, b):
            return gcd(b % a, a) if a != 0 else b
        
        pointsInLine = {}
        
        # idea:
        # calculate the representation of the line between all pairs of points
        # add points on the same line into a set
        # pointsInLine[a, b, c] = set of all indices of points lying on the line ax + by + c = 0
        # using indices to handle duplicates
        # return the size of the largest set
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1, x2, y2 = points[i][0], points[i][1], points[j][0], points[j][1]
                # line: ax + by + c = 0
                if x1 == x2:
                    # equation: x = x1
                    a, b, c = 1, 0, -x1
                else:
                    a, b, c = y2 - y1, x1 - x2, x2 * y1 - x1 * y2
                    # make sure a is positive
                    if a < 0:
                        a, b, c = -a, -b, -c
                    # get gcd of a, b and c
                    g = reduce(gcd, (a, b, c))
                    # reduce fraction
                    a, b, c = a/g, b/g, c/g
                line = (a, b, c)
                pointsInLine.setdefault(line, set())
                pointsInLine[line].add(i)
                pointsInLine[line].add(j)
        
        return max(len(points) for line, points in pointsInLine.items())