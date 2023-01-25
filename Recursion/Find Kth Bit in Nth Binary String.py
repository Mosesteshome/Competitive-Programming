#https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/
class Solution: 
    def findKthBit(self, n: int, k: int) -> str: 
        self.ans= ""
        self.past = {} 
        x = Solution.calc(self,n)
        x = x.replace(" ","")
        return x[k-1] 
    def calc(self,n)-> str:  
        if n == 1: 
            return "0"
        if (n) in self.past:
            return self.past[(n)]
        def inverse_f(x) -> str: 
            inverse_s  = " " 
            for i in x:  
                if i == '0': 
                    inverse_s += '1' 
                     
                elif i == "1": 
                    inverse_s += '0' 
            return inverse_s 
        self.past[(n)] =(str(Solution.calc(self,n-1)) + "1" + inverse_f(str(Solution.calc(self,n-1)))[::-1])
        return self.past[(n)]       
