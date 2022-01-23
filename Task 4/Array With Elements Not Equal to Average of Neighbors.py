//https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for x in range(1, len(nums) -1):

            if (nums[x-1] < nums[x] < nums[x+1]) or (nums[x-1] > nums[x] > nums[x+1]):
                nums[x+1], nums[x] = nums[x], nums[x+1]
                
        return nums
