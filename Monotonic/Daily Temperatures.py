#https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for x in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[x]:
                temp = stack.pop()
                answer[temp] = x-temp
            stack.append(x)
        return answer 
   