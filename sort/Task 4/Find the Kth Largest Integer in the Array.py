//https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/submissions/
class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        for i in range(0, len(nums)):
            nums[i] = int(nums[i])
        
        nums.sort(reverse=True)
        
        return str(nums[k-1])
