#https://leetcode.com/problems/find-original-array-from-doubled-array/
class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []
        for x in s:
            if x != ")":
                stack.append(x)
            else:
                temp=[]
                value = stack.pop()
                while value != "(":
                    temp.append(value)
                    value= stack.pop()
                print(temp)
                stack.extend(temp)
                
                
        
        return "".join(stack)
                
        
