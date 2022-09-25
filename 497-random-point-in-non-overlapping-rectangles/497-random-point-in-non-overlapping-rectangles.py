class Solution:

    def __init__(self, rects: List[List[int]]):
        w = [(x2-x1+1)*(y2-y1+1) for x1,y1,x2,y2 in rects]
        self.weights = [i/sum(w) for i in accumulate(w)]
        self.rects = rects

    def pick(self) -> List[int]:
        n_rect = bisect.bisect(self.weights, random.random())
        x1, y1, x2, y2 = self.rects[n_rect] 
        return [random.randint(x1, x2),random.randint(y1, y2)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()