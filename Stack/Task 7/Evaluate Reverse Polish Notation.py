#https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack =[]
        
        for x in tokens:
            if  x  not in {"+", "/", "*", "-"}:
                stack.append(int(x))
            else:
                
                var1 ,var2 = stack.pop(),(stack.pop())
                print(var2,var1)
                if x == '+':
                    stack.append(var1 + var2)
                elif x == '*':
                    stack.append(var1 * var2)                        
                elif x == '-':
                    stack.append(var2 - var1)                  
                elif x == '/':
                    if var1<0 and var2>0 or var1>0 and var2<0:
                        stack.append(-(abs(var2) / abs(var1)))
                    else:
                         stack.append((abs(var2) / abs(var1)))
                        
        return stack.pop()
                           
             

        
