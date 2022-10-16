class Solution:
    def calculate(self, s: str) -> int:
        stack, sign, num = [], '+', 0
        for i, c in enumerate(s + '+'):
            if c.isdigit():
                num = num * 10 + ord(c) - ord('0')
            elif c == '(':
                stack.append(sign)
                stack.append('(')
                sign = '+'
            elif c in '+-*/)':
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '/':
                    stack.append(int(stack.pop()/num))
                if c == ')':
                    num, item = 0, stack.pop()
                    while item != '(':
                        num += item
                        item = stack.pop()
                    sign = stack.pop()
                else:
                    sign, num = c, 0
        return sum(stack)