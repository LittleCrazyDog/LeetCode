class Solution:
    def nextClosestTime(self, time: str) -> str:
        hour, minute = time.split(':')
        # Generate all possible 2 digit values
        # There are all at most 16 sorted values here
        nums = sorted(set(hour+minute))
        two_digit_values = [a+b for a in nums for b in nums]
        
        # Check if the next valid minute is within the hour
        i = two_digit_values.index(minute)
        if i + 1 < len(two_digit_values) and two_digit_values[i+1] < '60':
            return hour + ':' + two_digit_values[i+1]
        
        # Check if the next valid hour is within the day
        i = two_digit_values.index(hour)
        if i + 1 < len(two_digit_values) and two_digit_values[i+1] < '24':
            return two_digit_values[i+1] + ':' + two_digit_values[0]
        
        # Return the earliest time of the next day
        return two_digit_values[0] + ':' + two_digit_values[0]