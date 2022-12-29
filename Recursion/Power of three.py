#https://leetcode.com/problems/power-of-three/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 3 or n == 1:
            return True
        elif n < 3:
            return False
        return (Solution.isPowerOfThree(self,n/3))
