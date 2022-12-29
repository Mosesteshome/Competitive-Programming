#https://leetcode.com/problems/power-of-four/
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return(Solution.calc(n))
    def calc(n) -> bool:
        if n == 4 or n == 1:
            return True
        elif n < 4:
            return False
        return(Solution.calc(n/4))