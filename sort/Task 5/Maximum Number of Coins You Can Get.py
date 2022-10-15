#https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
import itertools
class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
            """
        piles.sort()
        start, end = 0, len(piles)-1
        res = 0

        while start<end:
            res+=piles[end-1]
            end-=2
            start+=1
        return res

            
