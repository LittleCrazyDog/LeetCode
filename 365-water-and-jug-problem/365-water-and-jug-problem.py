class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        def gcd(x, y):
            if x < y:
                x, y = y, x
            while x != y and y != 0:
                remainder = x % y
                x = y
                y = remainder
            return x
        
        return targetCapacity == 0 or jug1Capacity + jug2Capacity >= targetCapacity and targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0