#https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue(object):

    def __init__(self):
        self.s1= []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.insert(0,x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.s1.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        return self.s1[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return True if not self.s1 else False

       
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
