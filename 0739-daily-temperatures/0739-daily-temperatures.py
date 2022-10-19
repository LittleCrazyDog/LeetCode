class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] #[temp,index]
       
        
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT,stackIndex = stack.pop()
                output[stackIndex] = i - stackIndex
            stack.append([t,i])
        return output