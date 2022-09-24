class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        for c in expression[::-1]:
            stack.append(c)
            if len(stack) >= 2 and stack[-2] == '?':
                boolean, _, t, _, f = stack.pop(), stack.pop(), stack.pop(), stack.pop(), stack.pop()
                stack.append(t if boolean == 'T' else f)
        return stack[0]