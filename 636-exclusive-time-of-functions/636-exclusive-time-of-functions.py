class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        
        for log in logs:
            fn, typ, time = log.split(':')
            fn, time = int(fn), int(time)
            
            if typ == 'start':
                stack.append(time)
            else:
                delta = time - stack.pop() + 1
                ans[fn] += delta
                stack = [t+delta for t in stack]
        
        return ans