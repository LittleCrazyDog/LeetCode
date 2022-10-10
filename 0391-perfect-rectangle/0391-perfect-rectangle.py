class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        corners = set()
        a, c = lambda: (X-x)*(Y-y), lambda: {(x,y),(x,Y),(X,y),(X,Y)}
        for x, y, X, Y in rectangles:
            area += a()
            corners ^= c()
        x, y, X, Y = (f(z) for f, z in zip((min, min, max, max), zip(*rectangles)))
        return area == a() and corners == c()