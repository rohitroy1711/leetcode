class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for i in ops:
            if i == "C":
                stack.pop()
            
            elif i=="D":
                stack.append(2*stack[-1])
                
            elif i=="+":
                stack.append(stack[-1]+stack[-2])
                
            else:
                stack.append(int(i))
        sum=0
        
        for i in stack:
            sum+=i
        return sum