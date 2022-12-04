#https://leetcode.com/problems/max-number-of-k-sum-pairs/
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort()
        count = 0 
        
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] + nums[j] == k:
                count += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] > k:
                j -= 1
            else:
                i +=1
        return count
