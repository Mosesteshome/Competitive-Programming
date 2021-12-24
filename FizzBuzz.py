class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        for x in range(1,n+1):
            temp = ""
        
            if (x%3==0):
                temp += "Fizz"
            if (x%5==0):
                temp += "Buzz"
            if not temp:
                temp = str(x)
            answer.append(temp)
        return answer
                
                
              
