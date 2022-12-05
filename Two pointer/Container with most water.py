#https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        i = 0
        j = len(height) -1
        while( i != j):
            temp = (j - i) * min(height[i],height[j])
            if( height[i] > height[j]):
                j -=1
            else:
                i += 1
            ans = max(ans,temp)
        return ans