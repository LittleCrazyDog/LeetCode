class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Max_length the longest subsequence without repeating chars and k changes
        # Max_count is the high count chars in the answer subsequence
        max_length = max_count = 0
        # Count keeps track of the chars in the we are looking at subsequence
        count = defaultdict(int)
        
        for i in range(len(s)):
            # Add char to the count dict
            count[s[i]] += 1
            # Key idea 2: Find the new max_count. Where we only consider if the new length exceedes the max_length overall
            max_count = max(max_count, count[s[i]])
            # Key idea 1: the answer is always max_cout + k
            if max_length < k + max_count:
                max_length += 1
            else:
                # Key idea 3: This removes the char at the start of the subsequence s[i-max_length]
                count[s[i-max_length]] -= 1
        
        return max_length
                