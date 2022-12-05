#https://leetcode.com/problems/validate-stack-sequences/submissions/
class Solution: 
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool: 
        ans = [] 
        j = 0 
        i = 1 
        ans.append(pushed[0])
        while ans or i <= len(pushed)-1:
            if ans and ans[-1] == popped[j]:
                ans.pop()
                j += 1
            elif i < len(pushed):
                ans.append(pushed[i]) 
                i += 1
            elif i == len(pushed) and ans[-1] != popped[j]:
                break
        if (ans):
            return (False)
        else:
            return (True)
