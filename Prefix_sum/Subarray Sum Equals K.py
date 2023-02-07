#https://leetcode.com/problems/subarray-sum-equals-k/description/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = prefix = 0
        d = {0:1}
        for i in nums:
            prefix += i
            if prefix -k in d:
                count += d[prefix - k]
            if prefix in d:
                d[prefix] += 1
            else:
                d[prefix] = 1
        return count 
            

