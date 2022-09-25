class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        mid = int(math.sqrt(area))
        while mid > 0:
            if area % mid == 0:
                return [area//mid, mid]
            mid -= 1