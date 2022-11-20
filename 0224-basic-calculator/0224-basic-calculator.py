class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        curRes = 0
        sign = 1
        s += '+'
        
        for ch in s:
            if ch.isdigit():
                num = num * 10 + ord(ch) - ord('0')
            elif not ch.isspace():
                if ch in '+-':
                    curRes += sign*num
                elif ch == '(':
                    stack.append((curRes, sign))
                    curRes = 0
                elif ch == ')':
                    curRes += sign*num
                    preNum, preSign = stack.pop()
                    curRes = preNum + preSign*curRes

                sign = -1 if ch == '-' else 1
                num = 0
        
        return curRes