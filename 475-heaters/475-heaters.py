class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # Go through houses and haters in ascending order. My i points to the current
        # closest heater. Go to the next heater if the current house coordinate is larger than
        # or equal to the middle between the current and the next heater
        heaters = sorted(heaters) + [float('inf')]
        i = r = 0
        for x in sorted(houses):
            while x >= sum(heaters[i:i+2]) / 2.:
                i += 1
            r = max(r, abs(heaters[i] - x))
        return r