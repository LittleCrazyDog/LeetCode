class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Sort the jobs by endTime
        # dp[time] = `profit` means that within the first time duration,
        # we can make at most `profit` money
        # Initial dp[0] = 0, as we make profit = 0 at time = 0.
        
        # For each jobs = [s, e, p], where s, e, p are its start time, end time and profit
        # Then the logic is similar to knapsack problem.
        # If we don't do this job, nothing will be changed.
        # If we do this job, binary search in the dp to find the largest profit we can make before start time s.
        # So we also know the maximum current profit that we can make doing this job.
        
        # Compare with last element in the dp,
        # we make more money,
        # it worth doing this job,
        # then we add the pair of [e, cur] to the back of dp
        # Otherwise, we'd like not to do this job
        
        # Complexity:
        # Time O(NlogN) for sorting
        # Time O(NlogN) for binary search for each job
        # Space O(N)
        
        jobs = sorted(zip(startTime, endTime, profit), key = lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s+1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]