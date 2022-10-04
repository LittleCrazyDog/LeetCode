class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for asteroid in asteroids:
            while len(res) and asteroid < 0 and res[-1] > 0:
                if res[-1] == -asteroid:
                    res.pop()
                    break
                if res[-1] > -asteroid:
                    break
                if res[-1] < -asteroid:
                    res.pop()
            else:
                res.append(asteroid)
        return res