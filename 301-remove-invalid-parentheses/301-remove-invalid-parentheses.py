class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        level = {s}
        while True:
            valid = []
            for elem in level:
                if self.valid(elem):
                    valid.append(elem)
            if valid:
                return valid
            
            next_level = set()
            # BFS
            for elem in level:
                for i in range(len(elem)):
                    next_level.add(elem[:i]+elem[i+1:])
            level = next_level
    
    def valid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0