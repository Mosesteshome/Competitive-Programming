#https://leetcode.com/problems/find-pivot-index/description/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i = 0
        left = 0
        right = sum(nums[i+1:])
        while i < len(nums)-1:
            if left == right:
                return i
 
            left += nums[i]
            right -= nums[i+1]
            i += 1
        if left == right:
            return len(nums)-1
        return -1

