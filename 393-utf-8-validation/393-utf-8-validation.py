class Solution:
    def validUtf8(self, data: List[int], start=0) -> bool:
        def check(data, start, size):
            for i in range(start+1, start+size+1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True
        
        while start < len(data):
            first = data[start]
            if (first >> 3) == 0b11110  and check(data, start, 3): start += 4
            elif (first >> 4) == 0b1110 and check(data, start, 2): start += 3
            elif (first >> 5) == 0b110  and check(data, start, 1): start += 2
            elif (first >> 7) == 0b0:                              start += 1
            else: 
                return False
        
        return True