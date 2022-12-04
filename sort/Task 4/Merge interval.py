#https://leetcode.com/problems/merge-intervals/
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        merge = []
        intervals.sort()
        j = 0
        for x in range(len(intervals)):
            if len(merge) == 0:
                merge.append([intervals[x][0],intervals[x][1]])
            else:
                
                if merge[j][1] >= intervals[x][0]:
                    
                    merge[j][1] = max(merge[j][1],intervals[x][1])
                else:
                    merge.append([intervals[x][0],intervals[x][1]])
                    j +=1
        return merge