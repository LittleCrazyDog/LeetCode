class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # 1. Convert each time to minutes. O(n)
        # 2. Sort the list of minutes. O(nlogn)
        # 3. Calculate the distance from p[i] to p[i+1] for all i except p[n-1] 
        #    where n is the length of the times array. O(n)
        # 4. Calculate the distance from the final point to it's first CW element, which will cross 0.
        #    This is the point in which there would be a revolution loop. O(1)
        
        # At each step between 3 and 4, minDist = min(current, new).
        
        timePoints = [60*int(time.split(':')[0])+int(time.split(':')[1]) for time in timePoints]
        
        timePoints.sort()
        
        res = float('inf')
        for i in range(0, len(timePoints)-1):
            res = min(res, (timePoints[i+1]-timePoints[i]))
        
        res = min(res, 60*24+timePoints[0]-timePoints[-1])
        
        return res