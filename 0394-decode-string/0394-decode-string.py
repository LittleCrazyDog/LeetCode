class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curString = ''
        curCount = 0

        for ch in s:
            if ch == '[':
                stack.append((curString, curCount))
                curString = ''
                curCount = 0
            elif ch == ']':
                prevString, prevCount = stack.pop()
                curString = prevString + prevCount*curString
                
            elif ch.isdigit():
                curCount = curCount * 10 + ord(ch) - ord('0')
            else:
                curString += ch
        
        return curString