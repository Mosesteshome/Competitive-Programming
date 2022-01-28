#https://leetcode.com/problems/min-stack/submissions/
class MinStack(object):

    def __init__(self):
        self.s1 = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.s1.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.s1.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.s1[-1]
    
        

    def getMin(self):
        """
        :rtype: int
        """
        #self.s1.sort()
        return  min(self.s1)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
