#https://leetcode.com/problems/minimum-increment-to-make-array-unique/
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        stack = []
        for i in nums:
            if stack and stack[-1]>=i:
                x = stack[-1] - i + 1
                ans += x
                stack.append(x+i)
            else:
                stack.append(i)
        return (ans)

    