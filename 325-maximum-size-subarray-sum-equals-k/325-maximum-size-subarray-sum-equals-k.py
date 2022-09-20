class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sum_to_index_mapping = {}   # key: cumulative sum till index i, value: i
        curr_sum = max_len = 0  # set initial values for cumulative sum and max length sum to k
        for i in range(len(nums)):
            curr_sum += nums[i] # update cumulative nums
            
            # two cases where we can update max_len
            if curr_sum == k:
                max_len = max(max_len, i+1) # case 1: cumulative sum is k, update max_len for sure
            elif curr_sum - k in sum_to_index_mapping:
                max_len = max(max_len, i - sum_to_index_mapping[curr_sum - k])  # case 2: cumulative sum is different from k, but we can truncate a prefix of the array
            
            # store cumulative sum in dictionary, only if it is not seen
            # because only the earlier (thus shorter) subarray is valuable, when we want to get the max_len after truncation
            if curr_sum not in sum_to_index_mapping:
                sum_to_index_mapping[curr_sum] = i
        
        return max_len